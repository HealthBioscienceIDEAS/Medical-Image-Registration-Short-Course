---
title: Setup
editor_options: 
  markdown: 
    wrap: sentence
---



## Accessing the materials for the practicals

* Create a folder in which you will store all of the material for the IPMI registration practicals, e.g. `C:\ipmi_reg\`
* If you haven't already, download the zip file containing data used in the practicals from moodle, [here](https://moodle.ucl.ac.uk/mod/resource/view.php?id=7158616).
* Extract the zip file in the folder you created above.
    * This will create the following folders containing the data used in the exercises:
        * `C:\impi_reg\data\practical1\CT_for_PET`
        * `C:\impi_reg\data\practical1\exhale_BH_CT`
        * `C:\impi_reg\data\practical1\inhale_BH_CT`
        * `C:\impi_reg\data\practical1\PET`
        * `C:\impi_reg\data\practical2`
        * `C:\impi_reg\data\practical3`
        * `C:\impi_reg\data\practical4`
* Download the following Python files (right click on the links and select 'Save link as...') and save them in the folder you created above.
    * [`practical1_notebook.ipynb`](files/practical1_notebook.ipynb)
    * [`practical2_notebook.ipynb`](files/practical2_notebook.ipynb)
    * [`practical3_notebook.ipynb`](files/practical3_notebook.ipynb)
    * [`practical4_notebook.ipynb`](files/practical4_notebook.ipynb)
    * [`utils.py`](files/utils.py) (used in practicals 2-4)
    * [`demonsReg.py`](files/demonsReg.py) (used in practical 4)


## Python Setup

Note - if you are taking the module MPHY0025 (IPMI) you are expected to have some familiarity and experience with Python. Anyone who has been using Python for a while, or has taken some kind of introductory course, should be fine.

### Creating an environment

We suggest creating a separate environment for the IPMI registration practicals. You can use this yml file: [`ipmi_reg_python_env.yml`](files/ipmi_reg_python_env.yml) to create a new environment with the required libraries, e.g. on the  Anaconda Prompt type:

``` 
conda env create --name ipmi_reg -f ipmi_reg_python_env.yml
```
This environment has been tested on all the tutorials and should help avoiding issues when running them.

### VSCode

You are welcome to use any Python IDE that you are familiar with for the practical session, but we recommend using VSCode, as it is a popular free IDE, and is what we used to develop and test the provided Jupyter notebooks and other Python code. 
You can download it [here](https://code.visualstudio.com/download).

We recommend looking at the following instructions to get started:

* [Python tutorial](https://code.visualstudio.com/docs/python/python-tutorial)
* [Instructions for Jupyter notebooks](https://code.visualstudio.com/docs/datascience/jupyter-notebooks)

#### Preparing VSCode for the practicals
* Start by opening the folder with the course content. Click 'File -> Open Folder...' and navigate to the `ipmi_reg` folder.

![](fig/setup-vscode-ipmi-reg-folder.png)

On the left, you can see the files available in the directory.

* Open one of the practicals (`.ipynb`). This is a Jupyter notebook.
    * If this is the first time you open a Jupyter notebook in VSCode, you may be prompted to install some extensions (Python, Pylance, Jupyter and a few more). If so, install them.
    * Note, you may not be promoted to install these extensions until you select the kernel (the next step).

* You now need to select the conda environment we created above. At the top right of the notebook, there should be a 'Select Kernel' button.
    * When you click this you may be prompted to install the extensions if you were not when you opened the Juypter notebook.
    
    ![](fig/setup-vscode-select-kernel-install-packages.png)

    * Once the extensions are installed, clicking 'Select Kernel' will then list two options:
        * 'Python Environments...'
        * 'Existing Jupyter Server...'
    * Click 'Python Environments...'. You should then see a dropdown menu with your existing environments. Select the `ipmi_reg` environment you created above.
    
    ![](fig/setup-vscode-select-kernel-ipmi-reg.png)

## Installing ITK-SNAP
ITK-SNAP started in 1999 with SNAP (SNake Automatic Partitioning) and was first developed by Paul Yushkevich with the guidance of Guido Gerig.
It is open-source software distributed under the GNU General Public License.
It is written in C++ and leverages the [Insight Segmentation and Registration Toolkit (ITK)](https://itk.org/).
ITK-SNAP will be used in Practical 1.

* The ITK-SNAP installer should be downloaded from [here](http://www.itksnap.org/pmwiki/pmwiki.php?n=Downloads.SNAP4).
    * Version 4.2.2 was used when preparing the practical exercises. Other versions can also be used for the practical, although they may behave slightly differently to what is described in the practical.
* Once you have downloaded the installer you should run it to install ITK-SNAP.
    * When you run the installer on Windows a window may pop up as shown below, with 'Don't run' as the only option given.
    
    ![](fig/setup-itk-snap-install-1.png)
    
    * However, If you click on 'More info' a new 'Run anyway' button will appear which you can click on to run the installer.
    
    ![](fig/setup-itk-snap-install-2.png)
    
    * Then all of the default options can be selected during installation.


