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
python NOA_getbbnet_automatic.py YYYY MM 
 
e.g for February 2017 

python NOA_getbbnet.py 2017 02 > Feb_2017.txt

### Revised (manual) locations
python NOA_getbbnet_manual.py YYYY MM 

e.g for January 2017

python NOA_getbbnet_manual.py 2017 01 >Jan_2017.txt

### Get data for an event
python NOA_getphases.py YYYY MM

e.g for January 2017

python NOA_getphases.py 2017 01 > Jan_2017.txt

