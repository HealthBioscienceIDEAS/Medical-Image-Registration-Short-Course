---
title: Setup
editor_options: 
  markdown: 
    wrap: sentence
---

````{=html}
<!--
## Github setup
1. You might have already a [GitHub](https://github.com), otherwise please [create one](https://github.com/join)
2. Generate your SSH keys as suggested [here](https://docs.github.com/en/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)
3. Clone the repository by typing (or copying) the following lines in a terminal
```
git clone git@github.com:HealthBioscienceIDEAS/Medical-Image-Registration-Short-Course.git
```
-->
````

## Course material

Start by downloading the course material [here](https://liveuclac-my.sharepoint.com/:u:/g/personal/rmapcdr_ucl_ac_uk/ETtoAQ1qXedMiU69mRdFXOIBcnKQ-nxMQ1c74gsPm7a6Sg?download=1).
Unzip it and make a note of where the folder is saved.

In this folder, you will find:

* A data directory which contains the datasets for each practical.
* 6 Jupyter notebooks with extensions `.ipynb` for each practical.
* 2 Python scripts with extensions `.py`.
* The `python-environment.yml` file which we will use in the steps below.

### Dataset
We provide a summary of the different datasets for each practical here. Datasets are described at the beginning of each practical. 

| Practical | Dataset |
|-------------------------------|-----------------------------------------|
| Practical 1 | [TCIA CT-vs-PET-Ventilation-Imaging](https://www.cancerimagingarchive.net/collection/ct-vs-pet-ventilation-imaging/) |
| Practical 2 | Lung MRI slice |
| Practical 3 | Head CT and MRI slices |
| Practical 4 | Lung MRI slices |
| Practical 5 | Dataset 5 |
| Practical 6 | Dataset 6 |

## Python Setup

### Installing Python

For Python beginners, we recommend installing miniconda [here](https://www.anaconda.com/download/success).
This provides a basic installation of Python and conda, which allows us to create virtual environments.
Once this has been installed, you should be able to open a terminal.

::::::::::::::::::::::::::::::::::::::::::: spoiler

### Opening a Terminal

* Windows: Click Start > Search for Anaconda Prompt > Click to Open
* macOS: Launchpad > Other Application > Terminal
* Linux: Open a terminal window

:::::::::::::::::::::::::::::::::::::::::::

### Creating an environment

Once you have opened the terminal, move to the location of the course files 
(use the `cd` command to move to the correct location - have a quick look [here](https://tutorials.codebar.io/command-line/introduction/tutorial.html) if you've never used the command line before). 

:::::::::::::::::::::::::: discussion
### What does this look like?
Say you have saved the extracted zip file on your Desktop. 
::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::: solution
### Windows
```
cd Desktop\ideas-reg\
```
Note: the above tutorial for the command line is for Mac/Linux users. 
In your Anaconda prompt in Windows, you can use `dir` instead of `ls` and `cd` without any arguments instead of `pwd`.
::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::: solution
### Mac/Linux
```bash
cd Desktop/ideas-reg/
```
::::::::::::::::::::::::::::::::::::

Create the environment from the existing `python-environment.yml` file.
``` bash
conda env create --name ideas-reg -f python-environment.yml
```
This environment has been tested on all the tutorials and should help avoiding issues when running them.

### VSCode

If you do not already have a Python IDE installed, we recommend using VSCode. 
It is very convenient as it allows us to open both Python scripts and Jupyter notebooks in the same interface.
You can download it [here](https://code.visualstudio.com/download).

We recommend looking at the following instructions to get started:

* [Python tutorial](https://code.visualstudio.com/docs/python/python-tutorial)
* [Instructions for Jupyter notebooks](https://code.visualstudio.com/docs/datascience/jupyter-notebooks)

#### Open the `ideas-reg` folder
Start by opening the folder with the course content. Go on `File --> Open Folder` and navigate to the `ideas-reg` unzipped folder.
![Figure. VSCode with ideas-reg opened](fig/vscode.png)

On the left, you can see the files available in the directory. Open one of the practicals (`.ipynb`). This is a Jupyter notebook.
If this is the first time you open a Jupyter notebook in VSCode, you should be prompted to install some extensions (Python, Pylance, Jupyter and a few more). 
Install them. 

#### Select the environment
You now need to select the conda environment we created above. At the top right of the notebook, there should be a `Select Kernel` button.
![Figure. VSCode: selecting an environment](fig/vscode-select-kernel.png)

Click on Python Environment. You should see a dropdown with your existing environments. Select `ideas-reg`.
![Figure. VSCode: selecting an environment](fig/vscode-ideas-reg.png)

## Software Setup

### ITK-SNAP
ITK-SNAP started in 1999 with SNAP (SNake Automatic Partitioning) and was first developed by Paul Yushkevich with the guidance of Guido Gerig.
It is open-source software distributed under the GNU General Public License.
It is written in C++ and leverages the [Insight Segmentation and Registration Toolkit (ITK)](https://itk.org/).
ITK-SNAP will be used in Practical 1.

* The ITK-SNAP installer should be downloaded from [here](http://www.itksnap.org/pmwiki/pmwiki.php?n=Downloads.SNAP4).
    * Version 4.2.2 was used when preparing the practical exercises. Other versions can also be used for the practical, although they may behave slightly differently to what is described in the practical.
* Once you have downloaded the installer you should run it to install ITK-SNAP.
    * When you run the installer on Windows a window may pop up as shown below, with 'Don't run' as the only option given.
    
    ![](fig/itk-snap-install-1.png)
    
    * However, If you click on 'More info' a new 'Run anyway' button will appear which you can click on to run the installer.
    
    ![](fig/itk-snap-install-2.png)
    
    * Then all of the default options can be selected during installation.


