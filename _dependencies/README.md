# Dependencies
* Using conda
```
conda create -n "mirVE" python=3.11 pip -c conda-forge
conda activate mirVE
cd /_dependencies
pip install -r requirements.txt
conda list -n mirVE #to check installed packages
conda remove -n mirVE --all #in case you want to remove it
```
* Using python virtual environment
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
cd /_dependencies
python3 -m pip install -r requirements.txt
```
