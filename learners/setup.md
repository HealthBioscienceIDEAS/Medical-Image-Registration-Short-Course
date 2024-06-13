---
title: Setup
---

FIXME: Setup instructions live in this document. Please specify the tools and
the data sets the Learner needs to have installed.

## Data Sets

<!--
FIXME: place any data you want learners to use in `episodes/data` and then use
       a relative link ( [data zip file](data/lesson-data.zip) ) to provide a
       link to it, replacing the example.com link.
-->
Download the [data zip file](https://example.com/FIXME) and unzip it to your Desktop

## Software Setup

### Installing Dependencies in Python Virtual environmnets
Installing python virtual environment with dependencies (e.g., nibabel, etc).
See further instructions [here](https://github.com/HealthBioscienceIDEAS/Medical-Image-Registration-Short-Course/tree/main/_dependencies). 

#### Using conda
```
conda create -n "mirVE" python=3.11 pip -c conda-forge
conda config --set pip_interop_enabled True
conda activate mirVE
cd ~/_dependencies
pip install -r requirements.txt
```

#### Using python virtual environment
```
# Installing dependencies in Ubuntu 22.04
sudo apt-get install -y python3-pip
sudo apt-get install -y python3-venv
# Create path for venv
cd $HOME
mkdir mirVE
cd mirVE
# Create virtual environment
python3 -m venv mirVE
source mirVE/bin/activate
cd ~/_dependencies
python3 -m pip install -r requirements.txt
```

### ITK-Snap

#### Hardware Requirements
* Memory: "Overall 2Gb of memory should be enough for most users; 4Gb should suffice for users with large images." [:link:](http://www.itksnap.org/pmwiki/pmwiki.php?n=Documentation.HardwareRequirements#:~:text=Memory%20usage%20in%20SNAP%20is,for%20a%20512%20cubed%20image.)
* Multi - Operating System: 
	* ITK-SNAP binaries are distributed for Linux (32 and 64 bit)), 
	* Windows (64 bit), 
	* and MacOS Leopard (64 bit).

#### Installation
##### Windows 11
- Open the following link: https://sourceforge.net/projects/itk-snap/files/itk-snap/4.2.0/
- Download `itksnap-4.2.0-20240422-win64-AMD64.exe` 
- Install it by following default settings.

##### Ubuntu 22.04 x64 GNU/Linux
```
FILENAME=itksnap-nightly-rel_4.0-Linux-gcc64.tar.gz  #Length: 200943059 (192M) [application/x-gzip]
cd ~/Downloads/
mkdir -p itksnap && cd itksnap
wget https://sourceforge.net/projects/itk-snap/files/itk-snap/Nightly/$FILENAME/download -O $FILENAME
tar -xvzf $FILENAME
```
#### Mac
```
TOADD
```


::::::::::::::::::::::::::::::::::::::: discussion

### Details

Setup for different systems can be presented in dropdown menus via a `solution`
tag. They will join to this discussion block, so you can give a general overview
of the software used in this lesson here and fill out the individual operating
systems (and potentially add more, e.g. online setup) in the solutions blocks.

:::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::: solution

### Windows

Use PuTTY

:::::::::::::::::::::::::

:::::::::::::::: solution

### MacOS

Use Terminal.app

:::::::::::::::::::::::::


:::::::::::::::: solution

### Linux

Use Terminal

:::::::::::::::::::::::::

