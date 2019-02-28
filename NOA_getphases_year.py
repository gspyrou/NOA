from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
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
    content = urllib2.urlopen('http://bbnet.gein.noa.gr/Events/{0}/{1}'.format(year,month)).read()
    soup = BeautifulSoup(content);
    for link in soup.find_all('a'):
            if link.has_attr('href'):
                if (link.text.find(".html")>0):
                    content =urllib2.urlopen('http://bbnet.gein.noa.gr/Events/{0}/{1}/{2}'.format(year,month,link.text)).read(); 
                #http://bbnet.gein.noa.gr//alerts_manual/{0}/{1}/{2}'.format(year,month,link['href'][1:])).read()
                    soup = BeautifulSoup(content);
                    data = soup.find("pre").text
                    if (data.find('Automatic Solution')<0):
                        print '\n'.join(data.split('\n')[2:])

        
