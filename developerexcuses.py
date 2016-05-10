import urllib2
from bs4 import BeautifulSoup
import time

def get_quote():
    response = urllib2.urlopen('http://developerexcuses.com/')
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    return soup.body.div.center.a.string

# while True:
#     print get_quote()
#     time.sleep(5)


print get_quote()
