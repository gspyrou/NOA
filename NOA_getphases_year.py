from bs4 import BeautifulSoup
import urllib2
import sys
import datetime

if len(sys.argv) > 1:
    year  = sys.argv[1]
else:
    now = datetime.datetime.now()
    year = now.year

months = ["01","02","03","04","05","06","07","08","09","10","11","12"]
for month in months:    
    content = urllib2.urlopen('http://bbnet.gein.noa.gr//alerts_manual/{0}/{1}/manual_alerts_{2}_{3}.html'.format(year,month,month,year)).read()
    soup = BeautifulSoup(content);
    for link in soup.find_all('a'):
            if link.has_attr('href'):
                    content =urllib2.urlopen('http://bbnet.gein.noa.gr//alerts_manual/{0}/{1}/{2}'.format(year,month,link['href'][1:])).read()
                    soup = BeautifulSoup(content);
                    print '\n'.join(soup.find("pre").text.split('\n')[2:])

        
