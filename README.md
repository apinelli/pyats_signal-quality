# CBR8 - US MER
## _Automatic retrieval of upstream measurements using pyATS_

```pyats_show_cable_sig_qual.py``` this is the python file used to parse US MER values from a given chassis and mac-domain. Accepts how many times the measurement should be taken as well as the interval between measurements.

```ShowCableSignalQualitytMer.py``` this is the parser developed for pyATS related to the command: ```show cable signal-quality mer```. A reference to write parsers for pyATS can be found here: https://pubhub.devnetcloud.com/media/pyats-development-guide/docs/writeparser/writeparser.html 

```yaml/cbr8_testbed_2.yaml``` is the testbed file (in yaml format) used as a reference for accessing the devices.

**Installation of pyATS:**
https://pubhub.devnetcloud.com/media/pyats-getting-started/docs/install/installpyATS.html
https://pubhub.devnetcloud.com/media/genie-docs/docs/installation/installation.html#installation
```
$ pip install pyats[full]
if 
  error: invalid command 'bdist_wheel'
  ----------------------------------------
  ERROR: Failed building wheel for yamllint
$ pip install --upgrade pip
$ pip install wheel

Installing genie: 
$ pip install genie
```
