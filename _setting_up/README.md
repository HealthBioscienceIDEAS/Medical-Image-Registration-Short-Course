# INSTRUCTIONS for installing R, Carpentries, and Sandpaper on Linux and Windows

## Steps in Ubuntu 22.04 x64
1. Create new repo: https://github.com/HealthBioscienceIDEAS/Medical-Image-Registration-Short-Course
2. Clone repo `git clone https://github.com/HealthBioscienceIDEAS/Medical-Image-Registration-Short-Course`
3. install R (if you haven't done already) [:link:](https://cran.r-project.org/bin/linux/ubuntu/) 
```
sudo apt-get install r-cran-xml
sudo apt-get install libxml2-dev
sudo apt install libgit2-dev
sudo apt install r-cran-curl

```
4. Open R and run the following to install dependencies
```
options(repos = c(
  carpentries = "https://carpentries.r-universe.dev/", 
  CRAN = "https://cran.rstudio.com/"
))
install.packages(c("remotes"), dep =TRUE)
```

5. In R, run 
```
remotes::install_github("HealthBioscienceIDEAS/sandpaper", dependencies = TRUE)
# this one is taking some 20mins the fist time as it seems is building various packages
# Terminal logs
Downloading GitHub repo HealthBioscienceIDEAS/sandpaper@HEAD
These packages have more recent versions available.
It is recommended to update all of them.
Which would you like to update?

1: All                                      
2: CRAN packages only                       
3: None                                     
4: pegboard (0.7.5 -> a32a7836d...) [GitHub]
5: varnish  (1.0.2 -> 56d594d27...) [GitHub]
6: curl     (4.3.2 -> 5.2.1       ) [CRAN]  
7: httr     (1.4.2 -> 1.4.7       ) [CRAN]  
8: gh       (1.3.0 -> 1.4.1       ) [CRAN]  
9: covr     (3.5.1 -> 3.6.4       ) [CRAN]  

Enter one or more numbers, or an empty line to skip updates: 1

The downloaded source packages are in
	‘/tmp/Rtmpn94NAu/downloaded_packages’
Downloading GitHub repo carpentries/pegboard@HEAD
These packages have more recent versions available.
It is recommended to update all of them.
Which would you like to update?

1: All                                        
2: CRAN packages only                         
3: None                                       
4: tinkr (0.2.0.9000 -> be564d524...) [GitHub]

Enter one or more numbers, or an empty line to skip updates: 1

── R CMD build ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
✔  checking for file ‘/tmp/Rtmpn94NAu/remotes50ddb31b7ca85/HealthBioscienceIDEAS-sandpaper-fb14e02/DESCRIPTION’ ...
─  preparing ‘sandpaper’:
✔  checking DESCRIPTION meta-information ...
─  checking for LF line-endings in source and make files and shell scripts (420ms)
─  checking for empty or unneeded directories
   Omitted ‘LazyData’ from DESCRIPTION
─  building ‘sandpaper_0.16.4.tar.gz’
   
Installing package into ‘/home/mxochicale/R/x86_64-pc-linux-gnu-library/4.4’
(as ‘lib’ is unspecified)
* installing *source* package ‘sandpaper’ ...
** using staged installation
** R
** inst
** byte-compile and prepare package for lazy loading
** help
*** installing help indices
*** copying figures
** building package indices
** installing vignettes
** testing if installed package can be loaded from temporary location
** testing if installed package can be loaded from final location
** testing if installed package keeps a record of temporary installation path
* DONE (sandpaper)
Warning message:
In i.p(...) : installation of package ‘curl’ had non-zero exit status

```

6. In R, run 
```
sandpaper::create_lesson("~/Desktop/medical-registration/Medical-Image-Registration-Short-Course")
## LOGS

> sandpaper::create_lesson("~/Desktop/medical-registration/Medical-Image-Registration-Short-Course")
No personal access token (PAT) available.gistration/Medical-Image-Registration-Short-Course...
Obtain a PAT from here:
https://github.com/settings/tokens
For more on what to do with the PAT, see ?gh_whoami.
ℹ No schedule set, using Rmd files in episodes/ directory.
→ To remove this message, define your schedule in config.yaml or use `set_episodes()` to generate it.
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
ℹ To save this configuration, use

set_episodes(path = path, order = ep, write = TRUE)
• Edit '/home/mxochicale/Desktop/medical-registration/Medical-Image-Registration-Short-Course/episodes/introduction.Rmd'
✔ First episode created in /home/mxochicale/Desktop/medical-registration/Medical-Image-Registration-Short-Course/episodes/introduction.Rmd
ℹ Workflows up-to-date!
✔ Lesson successfully created in ~/Desktop/medical-registration/Medical-Image-Registration-Short-Course
✔ Setting active project to '/home/mxochicale/Desktop/medical-registration/Medical-Image-Registration-Short-Course'
✔ Changing working directory to '/home/mxochicale/Desktop/medical-registration/Medical-Image-Registration-Short-Course/'
~/Desktop/medical-registration/Medical-Image-Registration-Short-Course
> 
```

7. Setting up config file in sandpaper template:
```
carpentry: 'IDEAS'
title: ''Medical-Image-Registration-Short-Course'
created: '2024-05-13'
source: 'https://github.com/HealthBioscienceIDEAS/Medical-Image-Registration-Short-Course'
varnish: 'HealthBioscienceIDEAS/varnish@IDEAS'
sandpaper: 'HealthBioscienceIDEAS/sandpaper@IDEAS'
```

8. Set up GitHub Pages 
* Go go [pages](https://github.com/HealthBioscienceIDEAS/Medical-Image-Registration-Short-Course/settings/pages) and select gh-pages branch with `/root` and click save
* Pass CI [actions](https://github.com/HealthBioscienceIDEAS/Medical-Image-Registration-Short-Course/actions/runs/9064118161)
* :tada: you have created: https://healthbioscienceideas.github.io/Medical-Image-Registration-Short-Course/


## Steps on Windows

### **INSTRUCTIONS for installing R, Carpentries, and Sandpaper on Windows:**

1. Create new repo: https://github.com/HealthBioscienceIDEAS/Medical-Image-Registration-Short-Course

2. Clone repo `git clone https://github.com/HealthBioscienceIDEAS/Medical-Image-Registration-Short-Course`

3. Installing R using the following: https://cran.r-project.org/bin/windows/base/

4. Using the default settings during the installation of **RGUi 4.x.x**

5. From RGui Console, enter the following command: 
```
options(repos = c(
carpentries = "https://carpentries.r-universe.dev/",
CRAN = "https://cran.rstudio.com/"
))
```

6. Enter the following command: 
`remotes::install_github("HealthBioscienceIDEAS/sandpaper", dependencies = TRUE)
`
7. Change path from RGUi to the GitHub folder of the medical image registration course. This is done from the Menu list by picking 'File' then 'Change Dir..'

8. Run the following command to start sandpaper: 
`sandpaper::build_lesson()
`
9. You may notice some package not installed called _**Pandoc**_ after running the sandpaper command. If so, install Pandoc then run _step 8_ again.
Pandoc installation: https://pandoc.org/installing.html



## Steps in MAC
Packages via homebrew: freetype, fribidi, harfbuzz, libpng, git2. 

