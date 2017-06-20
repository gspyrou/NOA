# download AUTO catalog from NOA

from bs4 import BeautifulSoup
import datetime
import urllib2
import sys

if len(sys.argv) > 2:
    year  = sys.argv[1]
    month = sys.argv[2]
else:
    now = datetime.datetime.now()
    year = now.year
    month = '{:02d}'.format(now.month)

baseUrl = 'http://bbnet.gein.noa.gr/alerts_manual/{0}/{1}/manual_alerts_{2}_{3}.html'.format(year,month,month ,year)

content = urllib2.urlopen(baseUrl).read()

soup = BeautifulSoup(content,"html5lib")


for trs in soup.find_all('tr')[1:]:
    tds = trs.find_all('td')
    row = [elem.get_text().strip().encode('utf-8') for elem in tds]
    if row: 
        print row
       
 
