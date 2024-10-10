---
title: Setup
---

<!--
## Github setup
1. You might have already a [GitHub](https://github.com), otherwise please [create one](https://github.com/join)
2. Generate your SSH keys as suggested [here](https://docs.github.com/en/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)
3. Clone the repository by typing (or copying) the following lines in a terminal
```
git clone git@github.com:HealthBioscienceIDEAS/Medical-Image-Registration-Short-Course.git
```
-->


## Python Setup
### Installing Python
Include instructions to download miniconda and recommendations for an IDE.
<!--
Add instructions for Jupyter notebooks if used.
-->

### Installing Dependencies in Python Virtual environments
Installing python virtual environment with dependencies (e.g., nibabel, etc).
See further instructions [here](https://github.com/HealthBioscienceIDEAS/Medical-Image-Registration-Short-Course/tree/main/_dependencies). 

```bash
conda create -n "mirVE" python=3.11 pip -c conda-forge
conda config --set pip_interop_enabled True
conda activate mirVE
cd ~/_dependencies
pip install -r requirements.txt
```

Install file with in-built functions pip install *.


## Software Setup
### ITK-SNAP
<!-- add link? -->
ITK-SNAP started in 1999 with SNAP (SNake Automatic Partitioning) and developed by Paul Yushkevich with the guidance of Guido Gerig. 
It is open-source software distributed under the GNU General Public License.
It is written in C++ and it leverages the Insight Segmentation and Registration Toolkit (ITK) library. 
ITK-SNAP will be used in Practical 1.

<!--
#### Hardware Requirements
* Memory: "Overall 2Gb of memory should be enough for most users; 4Gb should suffice for users with large images." [:link:](http://www.itksnap.org/pmwiki/pmwiki.php?n=Documentation.HardwareRequirements#:~:text=Memory%20usage%20in%20SNAP%20is,for%20a%20512%20cubed%20image.)
* Multi - Operating System: 
	* ITK-SNAP binaries are distributed for Linux (32 and 64 bit)), 
	* Windows (64 bit), 
	* and MacOS Leopard (64 bit).
-->

::::::::::::::::::::::::::::::::::::::: discussion

### Installation
Below are instructions to install ITK-SNAP in different operating systems.

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
```bash
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


## Dataset
<!--
FIXME: place any data you want learners to use in `episodes/data` and then use
       a relative link ( [data zip file](data/lesson-data.zip) ) to provide a
       link to it, replacing the example.com link.
-->
Data for this course can be downloaded here [data zip file](https://example.com/FIXME). Data for all practicals can be found there. Datasets are labelled in the table and are described at the beginning of each practical.

| Practical  | Dataset        |
|------------|----------------|
| Practical 1| [TCIA CT-vs-PET-Ventilation-Imaging](https://www.cancerimagingarchive.net/collection/ct-vs-pet-ventilation-imaging/) |
| Practical 2| Lung MRI slice      |
| Practical 3| Head CT and MRI slices      |
| Practical 4| Dataset 4      |
| Practical 5| Dataset 5      |
| Practical 6| Dataset 6      |




