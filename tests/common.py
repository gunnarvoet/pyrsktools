#!/usr/bin/env python3
# Standard/external imports
from typing import *
import json
import numpy as np
import numpy.typing as npt
from pathlib import Path
from timeit import default_timer

# Module imports
from pyrsktools import RSK

_HERE = Path(__file__).parent.resolve()
_RSK_DIR = _HERE / "rsks/rsktools"
_CSV_DIR = _RSK_DIR / "csv"
_VERSION_DIR = _RSK_DIR / "version"

RSK_FILES: Tuple[Path] = tuple(_RSK_DIR.glob("*.rsk"))
RSK_FILES_PROFILING: Tuple[Path] = tuple(_RSK_DIR.glob("*profiling.rsk"))
RSK_FILES_MOOR: Tuple[Path] = tuple(_RSK_DIR.glob("*moor.rsk"))
RSK_FILES_VERSION: Tuple[Path] = tuple(_VERSION_DIR.glob(".rsk"))

GOLDEN_RSK: Path = _RSK_DIR / "EPd_wave_2.0.0_profiling.rsk"
GOLDEN_RSK_TYPE: str = "EPdesktop"
GOLDEN_RSK_VERSION: str = "2.0.0"

CSV_FILES: Tuple[Path] = tuple(_CSV_DIR.glob("*.csv"))
GOLDEN_CSV: Path = _CSV_DIR / "minimal_ctd.csv"

MATLAB_RSK: Path = _RSK_DIR / "ful_cont_2.18.2_profiling.rsk"
MATLAB_DATA_DIR: Path = _RSK_DIR / "mRSKtools_data"

MATLAB_RSK_MOOR: Path = _RSK_DIR / "ful_cont_2.18.2_moor.rsk"
MATLAB_DATA_DIR_MOOR: Path = _RSK_DIR / "mRSKtools_data"

BPR_RSK: Path = _RSK_DIR / "ful_cont_2.18.2_BPR.rsk"
APT_CERVELLO_RSK: Path = _RSK_DIR / "ful_cont_2.15.0_APT_cervello.rsk"

assert _RSK_DIR.exists() and _RSK_DIR.is_dir()
assert len(RSK_FILES) > 0
assert GOLDEN_RSK.exists() and GOLDEN_RSK.is_file()

assert _CSV_DIR.exists() and _CSV_DIR.is_dir()
assert len(CSV_FILES) > 0
assert GOLDEN_CSV.exists() and GOLDEN_CSV.is_file()

assert MATLAB_DATA_DIR.exists() and MATLAB_DATA_DIR.is_dir()


class Timer:
    def __init__(self, verbose: bool = False):
        self.verbose = verbose
        self.timer = default_timer
        self.start = 0
        self.end = 0
        self.elapsed = 0  # milliseconds elapsed

    def __enter__(self):
        self.start_timer()
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.stop_timer()

    def start_timer(self):
        self.start = self.timer()

    def stop_timer(self):
        self.end = self.timer()
        self.elapsed = (self.end - self.start) * 1000
        if self.verbose:
            print(f"Elapsed time: {self.elapsed} ms")


def readMatlabFile(fileName: str) -> dict:
    mFile = MATLAB_DATA_DIR / fileName
    with mFile.open("r") as fd:
        mRSK = json.load(fd)

    return mRSK


def readMatlabProfileDataWithNaN(fileName: str) -> dict:
    mFile = MATLAB_DATA_DIR / fileName
    with mFile.open("r") as fd:
        mRSK = json.load(fd)
        mData = mRSK["data"]
        for i in range(len(mData)):
            d = mData[i]["values"]
            for ii in range(len(d)):
                d0 = d[ii]
                for iii in range(len(d0)):
                    if d0[iii] is None:
                        d0[iii] = np.nan
        mRSK["data"] = mData
    # for ii in range(len(mData)):
    #     d = mData[ii]["values"]
    #     [[v if v is not None else np.nan for v in nested] for nested in d]

    return mRSK


def readMatlabIndices(fileName: str) -> list:
    mFile = MATLAB_DATA_DIR / fileName
    with mFile.open("r") as fd:
        mIdx = json.load(fd)
    return mIdx


def readMatlabChannelDataByName(
    mRSK: dict,
    channelName: str,
    profiles: Union[int, Collection[int]] = [],
    direction: str = "both",
) -> Union[npt.NDArray, List[npt.NDArray]]:
    i = [
        i
        for i in range(len(mRSK["channels"]))
        if mRSK["channels"][i]["longName"].lower() == channelName.lower()
    ][0]

    try:
        return np.array(mRSK["data"]["values"], dtype="float64")[:, i]
    except TypeError:
        profileData = []
        profiles = {profiles} if profiles and isinstance(profiles, int) else set(profiles)
        mData = mRSK["data"]
        for j in range(0, len(mData), 2):
            profileIndex = j // 2
            down = mData[j]["values"] if mData[j]["direction"] == "down" else mData[j + 1]["values"]
            down = np.array(down)[:, i]  # The channel (i) data as an array
            up = mData[j]["values"] if mData[j]["direction"] == "up" else mData[j + 1]["values"]
            up = np.array(up)[:, i]

            if not profiles or profileIndex in profiles:
                if direction == "down":
                    profileData.append(down)
                elif direction == "up":
                    profileData.append(up)
                else:
                    profileData.append(np.concatenate((down, up)))

        return profileData


def getProfileData(
    pyRSK: RSK, mRSK: dict, trim: int = 1
) -> Iterator[Tuple[npt.NDArray, npt.NDArray]]:
    upIndices = pyRSK.getprofilesindices(direction="up")
    downIndices = pyRSK.getprofilesindices(direction="down")

    # mRSKtools stores all profile data in one array (of arrays), with
    # each profile (up AND down, if "both" was selected) being an element
    # in this array. We always use "both" to generate mRSKtools data, so
    # the array should be len(up) + len(down) profiles.
    assert len(upIndices) + len(downIndices) == len(mRSK["data"])

    # Iterate the length of mRSK data, but increment by two so we
    # compare both up and down at the same time.
    mDownIsFirst = mRSK["data"][0]["direction"] == "down"
    for i in range(0, len(mRSK["data"]), 2):
        if mDownIsFirst:
            mDownIndex, mUpIndex = i, i + 1
        else:
            mUpIndex, mDownIndex = i, i + 1

        # mRSKtools down profile
        mDownData = np.array(mRSK["data"][mDownIndex]["values"])
        # mRSKtools up profile
        mUpData = np.array(mRSK["data"][mUpIndex]["values"])
        # pyRSKtools down profile
        pyDownData = pyRSK.data[downIndices[i // 2]]
        # pyRSKtools up profile
        pyUpData = pyRSK.data[upIndices[i // 2]]

        # Compare data for each channel
        channelNames = pyRSK.channelNames
        # But let's store all channel data into one big array
        # (i.e., collect all channel data for each profile together)
        # and yield that to the caller
        pyProfileData = []
        mProfileData = []
        for j in range(len(channelNames)):
            # pyChannelData = np.concatenate((pyDownData[channelNames[j]], pyUpData[channelNames[j]]))
            # mChannelData = np.concatenate((mDownData[:, j],  mUpData[:, j]))

            pyChannelData = np.concatenate(
                (pyDownData[channelNames[j]][:-trim], pyUpData[channelNames[j]][:-trim])
            )
            mChannelData = np.concatenate((mDownData[:-trim, j], mUpData[:-trim, j]))

            pyProfileData.append(pyChannelData)
            mProfileData.append(mChannelData)

        # Yield all data for current profile to caller so they can compare values
        yield np.asarray(pyProfileData), np.asarray(mProfileData)
