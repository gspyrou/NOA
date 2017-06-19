# Seismological data from National Observatory of Athens
## Prerequisites
### Install Python 2.7
https://www.python.org/download/releases/2.7/
### Install BeautifulSoup 
pip install beautifulsoup4
### Install html5lib parser
pip install html5lib

## Download data
### Automatic locations
python NOA_getbbnet.py <YYYY> <MM> automatic
 
e.g for February 2017 

python NOA_getbbnet.py 2017 02 automatic

### Revised (manual) locations
python NOA_getbbnet.py <YYYY> <MM> manual

e.g for January 2017

python NOA_getbbnet.py 2017 01 manual

