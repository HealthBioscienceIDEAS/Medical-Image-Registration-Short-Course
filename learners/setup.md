---
title: Setup
---


## Github setup
1. You might have already a [GitHub](https://github.com), otherwise please [create one](https://github.com/join)
2. Generate your SSH keys as suggested [here](https://docs.github.com/en/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)
3. Clone the repository by typing (or copying) the following lines in a terminal
```
git clone git@github.com:HealthBioscienceIDEAS/Medical-Image-Registration-Short-Course.git
```

## Dataset

<!--
FIXME: place any data you want learners to use in `episodes/data` and then use
       a relative link ( [data zip file](data/lesson-data.zip) ) to provide a
       link to it, replacing the example.com link.
-->
Download the [data zip file](https://example.com/FIXME) and unzip it to your Desktop

### CT-vs-PET-Ventilation-Imaging 
CT Ventilation as a Functional Imaging Modality for Lung Cancer Radiotherapy from [TCIA](https://www.cancerimagingarchive.net/collection/ct-vs-pet-ventilation-imaging/).
We recomend to focus on exhale/inhale breath hold CT (BHCT) Dicoms which belog to: 
* The BHCT scans for CT-PET-VI-02 & CT-PET-VI-03 show very little motion between inhale and exhale
* The BHCT scans for CT-PET-VI-05 have a different number of slices between the inhale and exhale


Data paths look like these:
```
/CT-PET-VI-02$ tree -d 
.
├── 1000.000000-PET SUV Factors-26496 [1 item, with size 42.1 kB]
├── 3.000000-CT Lung  3.0  B31f-61322  [175 items, totalling 92.4 MB]
├── 4.000000-Galligas Lung-03537 [159 items, totalling 51.5 MB]
├── 5.000000-Thorax Insp  2.0  B70f-29873 [167 items, totalling 88.1 MB]
├── 7.000000-Thorax Exp  2.0  B70f-73355 [167 items, totalling 88.1 MB]
└── 8.000000-RespLow  2.0  B30s  80  Ex - 100  In-44317 [810 items, totalling 426.9 MB]

/CT-PET-VI-03$ tree -d
.
├── 06-25-1996-RTRTRespLowBreathRateRNS Adult-43080
│   ├── 1000.000000-PET SUV Factors-06580
│   ├── 3.000000-CT Lung  3.0  B31f-08354
│   └── 4.000000-Galligas Lung-15379
└── 06-25-1996-RTRTRespLowBreathRateRNS Adult-87093
    ├── 5.000000-Thorax Insp  2.0  B70f-42000
    ├── 7.000000-Thorax Exp  2.0  B70f-45310
    └── 8.000000-RespLow  2.0  B30s  80  Ex - 100  In-54790

/CT-PET-VI-05$ tree -d
└── 12-10-1996-RTRTRespLowBreathRateRNS Adult-37585
    ├── 1000.000000-PET SUV Factors-63910
    ├── 3.000000-CT Lung  3.0  B31f-90638
    ├── 4.000000-Galligas Lung-26361
    ├── 5.000000-Thorax Insp  2.0  B70f-45546
    ├── 7.000000-Thorax Exp  2.0  B70f-31579
    └── 8.000000-RespLow  2.0  B30s  80  Ex - 100  In-16454
```



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


::::::::::::::::::::::::::::::::::::::: discussion

### Installation

Installing ITK-SNAP in differen operating systems

:::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::: solution

### Windows

- Open the following link: https://sourceforge.net/projects/itk-snap/files/itk-snap/4.2.0/
- Download `itksnap-4.2.0-20240422-win64-AMD64.exe` 
- Install it by following default settings.

:::::::::::::::::::::::::


:::::::::::::::: solution

### Linux (tested on Ubuntu 22.04 x64 GNU/Linux)

- Open your Terminal to install it
```
sudo apt-get install tree # to visualise files and paths
FILENAME=itksnap-nightly-rel_4.0-Linux-gcc64.tar.gz  #Length: 200943059 (192M) [application/x-gzip]
cd ~/Downloads/
mkdir -p itksnap && cd itksnap
wget https://sourceforge.net/projects/itk-snap/files/itk-snap/Nightly/$FILENAME/download -O $FILENAME
tar -xvzf $FILENAME
```

:::::::::::::::::::::::::


:::::::::::::::: solution

### MacOS

- Open the following link: https://sourceforge.net/projects/itk-snap/files/itk-snap/4.2.0/ and download  `itksnap-4.2.0-20240422-Darwin-x86_64.dmg`	
- Double click the icon for the file you downloaded (e.g., itksnap-3.2.0-rc2-20140919-MacOS-x86_64.dmg).
- Drag the icon ITK-SNAP.app to the Applications folder.
- Drag the icon itksnap on top of the icon `usr_local_bin` in that folder.
- To add the ITK-SNAP launcher to your Dock, open the Applications folder and drag the ITK-SNAP.app icon onto the dock.

:::::::::::::::::::::::::

