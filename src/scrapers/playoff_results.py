from bs4 import BeautifulSoup
import urllib2

req = urllib2.urlopen('http://www.basketball-reference.com/playoffs/')
soup = BeautifulSoup(req, 'html.parser')
soup.tbody.find_all('td')
#do some pattern processing on the list ^