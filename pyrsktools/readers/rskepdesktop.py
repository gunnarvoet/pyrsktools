#!/usr/bin/env python3
# Standard/external imports
from typing import *
import sqlite3
import dataclasses

# Module imports
from pyrsktools.readers import Reader
from pyrsktools.utils import semver2int, rsktime2datetime
from pyrsktools.datatypes import *


class RSKEPDesktopReader(Reader):
    TYPE: str = "EPdesktop"
    MIN_SUPPORTED_SEMVER: str = "1.13.4"
    MAX_SUPPORTED_SEMVER: str = "2.18.2"

    def calibrations(self: Reader) -> List[Calibration]:
        datatype, table = Calibration, "calibrations"

        # NOTE: below is a modified version of self._createDatatypesFromQuery()
        results = []
        datatypeFields: dict = {}
        commonFields: Set[str] = set()

        for row in self._query(table):
            if not datatypeFields:
                datatypeFields = {field.name: field.type for field in dataclasses.fields(datatype)}
                commonFields = set(row.keys()).intersection(datatypeFields.keys())

            fieldsDict = {
                field: row[field]
                if datatypeFields[field] != "datetime64"
                else rsktime2datetime(row[field])
                for field in commonFields
            }

            # In EPdesktop RSKs, there are a variable number of coefficient
            # columns in the calibrations table. The below grabs all that exist.
            # For dictionaries below, key is coefficient number and value are...coef value.
            if self.version >= semver2int("2.10.0"): # NOTE: need to know when full and EPdesktop schema merged (known: 2.18.2, they are the same)
                # For 2.18.2, EPdesktop schema = full schema
                coefTable = "coefficients"
                calibrationID = fieldsDict["calibrationID"]

                # For dictionaries below, key is coefficient number and value are...coef value.
                fieldsDict["c"], fieldsDict["x"], fieldsDict["n"] = {}, {}, {}
                for cRow in self._query(
                    coefTable, where=f"calibrationID = {calibrationID}", orderByAsc="key"
                ):
                    coefKey = int(cRow["key"][1:])
                    coefValue = np.nan if cRow["value"] is None else cRow["value"]

                    if cRow["key"].startswith("c"):
                        fieldsDict["c"][coefKey] = float(coefValue)
                    elif cRow["key"].startswith("x"):
                        fieldsDict["x"][coefKey] = float(coefValue)
                    elif cRow["key"].startswith("n"):
                        fieldsDict["n"][coefKey] = int(coefValue)
                    else:
                        raise ValueError(
                            f"Unsupported coefficient type found in '{coefTable}' table: {coefKey}"
                        )
                results.append(datatype(**fieldsDict))

            else:
                for coefPrefix in ("c", "x", "n"):
                    fieldsDict[coefPrefix] = {
                        int(field[1:]): np.nan
                        if row[field] is None
                        else (int(row[field]) if coefPrefix == "c" else float(row[field]))
                        for field in row.keys()
                        if field.startswith(coefPrefix) and field[1:].isnumeric()
                    }

                instance = datatype(**fieldsDict)
                results.append(instance)

        return results
