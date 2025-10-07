########## 
Changelog
##########

Release 1.1.2
==============================

2025-10-06

* DeriveSA now recognizes latitude and longitude at 0 correctly
* Fixed a bug where channels' derived status were processed improperly
* Fixed a bug where the region profile order was calculated incorrectly
* Fixed a bug where the region profile order was read incorrectly from the RSK file
* Fixed a bug where the alignchannels encountered an error when lagunit == 'seconds'
* Fixed a bug where RSK.trim removed incorrect profile indices

Release 1.1.1
==============================

2022-11-09

* Support "EPdesktop" RSK files up to the latest version (from v1.13.4 to v2.18.2)

Release 1.1.0
==============================

2022-09-09

* New method `RSK.deriveAPT()`_ to derive triaxial accelerations and temperature from the accelerometer period data
* pyRSKtools now supports reading data from RBR *cervello* and RBR *cervata*

Release 1.0.0
==============================

2022-08-22

* Initial release 🎉


.. _RSK.deriveAPT(): https://docs.rbr-global.com/pyrsktools/_rsk/process.html#deriveapt