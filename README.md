
# MatriSIMS

GUI Python application to fit and process SIMS data for minerals with matrix effect.


## Introduction

This software is meant to calibrate matrix effect for SIMS analyses of minerals or glass with complex major element composition. It allows the automatic propagation of the uncertainty on the measured isotopic composition and the uncertainty on the fit for sample data.

![name-of-you-image](https://github.com/G-Siron/MatriSIMS/blob/main/Screenshots/Screen_Shot_MatriSIMS_Layout_v2.png)


## Setup

Once you have cloned or downloaded the repository, navigate through the terminal to the correct folder. It is strongly recommended to install it through a virtual environment to avoid any discrepancies with previsouly installed packages versions that you would need to run other scripts. You can do this inside a virtual environement using venv
```
python3 -m venv venv
```
Then activate the virtual environement
```
# On Mac/Linux:
source venv/bin/activate
# On Windows:
call venv\scripts\activate.bat
```
Then, install all Python packages needed to run MatriSIMS throught he folowing command
```
pip install requirements.txt
```

## Run MatriSIMS

To start the application, when in the correct folder (and with your virtual environement activated if you want to work in one)
```
python3 Matrix_SIMS.py
```

## Authors

- Guillaume Siron [@G-Siron](https://github.com/G-Siron)

