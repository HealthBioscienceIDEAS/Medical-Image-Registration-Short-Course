# How to setup local previews of the Workbench website

## Installing requirements
### Windows/Mac
1. If R is not already installed, install R using the following: 
   * [Windows](https://cran.r-project.org/bin/windows/base/) and use the default settings during the installation of **RGUi 4.x.x**
   * [Mac](https://cran.r-project.org/bin/macosx/)
1. **Optional, but recommended** Download [RStudio Desktop](https://posit.co/download/rstudio-desktop/)
1. **For Mac only** Before installing Varnish and Sandpaper, there are some 
additional packages that will need to be installed. The easiest way is via 
[Homebrew](https://brew.sh/):
   ```bash
   brew install freetype fribidi harfbuzz libpng libgit2
   ```
1. Open RStudio and run the following lines of code to install the sandpaper package. 
   ```r
   options(repos = c(
     carpentries = "https://carpentries.r-universe.dev/", 
     CRAN = "https://cran.rstudio.com/"
   ))
   install.packages("sandpaper", dep = TRUE)
   ```
   You can find further instructions on the
[Carpentries Workbench documentation](https://carpentries.github.io/sandpaper-docs/index.html)
1. Enter the following command to install the local version of varnish. This
version is needed to incorporate the IDEAS identity for the site. 
   ```r
   install.packages("remotes")
   remotes::install_github("HealthBioscienceIDEAS/varnish", dependencies = TRUE)
   ```
1. Go to the section on [previewing the website](#previewing-episodes)

### Linux
This installation was performed using Ubuntu 22.04 x64

1. install R (if you haven't done already) from  [CRAN](https://cran.r-project.org/bin/linux/ubuntu/) 
   ```bash
   sudo apt-get install r-cran-xml
   sudo apt-get install libxml2-dev
   sudo apt install libgit2-dev
   sudo apt install r-cran-curl
   ```
1. OPen R and install the sandpaper package. 
   ```r
   options(repos = c(
     carpentries = "https://carpentries.r-universe.dev/", 
     CRAN = "https://cran.rstudio.com/"
   ))
   install.packages("sandpaper", dep = TRUE)
   ```
1. Install the local IDEAS fork of the varnish repository
   ```r
   install.packages("remotes")
   remotes::install_github("HealthBioscienceIDEAS/varnish", dependencies = TRUE)
   # this one takes a long time, about 20mins for the the fist time 
   # due to dependencies
   # You may see something similar to below in the output of the terminal
   # (this has been truncated - a fair amount of additional text should
   # follow showing progress of the installation)
   
   Downloading GitHub repo HealthBioscienceIDEAS/varnish@HEAD
   These packages have more recent versions available.
   It is recommended to update all of them.
   Which would you like to update?

   1: All                                      
   2: CRAN packages only                       
   3: None
   ...(individual packages)

   Enter one or more numbers, or an empty line to skip updates: 1
   ...(truncated)
   ```
## Previewing episodes
### In your local machine
1. Using your terminal clone repo
   ```bash
   git clone git@github.com:HealthBioscienceIDEAS/Medical-Image-Registration-Short-Course.git 
   ```
1. If you are working on a specific branch, checkout the branch locally:
   ```bash
   git checkout feature-branch-name
   ``` 
1. In RStudio, open the medical imaging regsitration course repository by going to
File->Open Project and then selecting the path where you cloned the repository.
You may need to click on the R project file that is located in the repository directory.
1. Run the following command to start sandpaper: 
    ```r
   sandpaper::serve()
   ```
   This will build the site and put it in the `Viewer` tab in RStudio. You can look at it in your
   browser by clicking on the "Open in New Window" icon.
   
   If you notice errors that the package _**Pandoc**_  was not installed, try installing Pandoc and
   then try building the lesson again. If successful, R which will launch your internet browser with the episode.
   As you make edits and save the document you are working on, the site will be rebuilt.

   **Alternative to sandpaper::serve**
   
   The function `build_lesson` is very similar to 
   ```r
   sandpaper::build_lesson()
   ```
   except that it doesn't automatically build upon each save. If the page does not appear automatically in
   your browser, you may need to open it manually. 

### On GitHub
You can also preview your episodes once you have a Pull-Request.

Select branch called md-outputs-<PR-number> for each PR where it stores the 
rendered markdown files. This is controlled by the [pr-receive](https://carpentries.github.io/sandpaper-docs/pull-request.html#reviewing-a-pull-request) workflow. 

Note this will only preview the markdown, it will not look like the final
rendered website.

