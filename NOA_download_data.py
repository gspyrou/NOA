from bs4 import BeautifulSoup
import urllib2
import sys
import datetime

if len(sys.argv) > 2:
    year  = sys.argv[1]
    month = sys.argv[2]
else:
    now = datetime.datetime.now()
    year = now.year
    month = '{:02d}'.format(now.month)

content = urllib2.urlopen('http://bbnet.gein.noa.gr//alerts_manual/{0}/{1}/manual_alerts_{2}_{3}.html'.format(year,month,month,year)).read()
soup = BeautifulSoup(content,'html5lib');
for link in soup.find_all('a'):
        if link.has_attr('href'):
                content =urllib2.urlopen('http://bbnet.gein.noa.gr//alerts_manual/{0}/{1}/{2}'.format(year,month,link['href'][1:])).read()
                soup = BeautifulSoup(content);
                print '\n'.join(soup.find("pre").text.split('\n')[2:])
