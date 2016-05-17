import urllib2
from bs4 import BeautifulSoup
import time


def get_quote():
    response = urllib2.urlopen('http://developerexcuses.com/')
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    return soup.body.div.center.a.string

quotefile = open('d.txt', 'r+')

while True:
    quotefile.seek(0, 0)
    content = quotefile.read()
    new_quote = get_quote()
    if new_quote not in content:
        print new_quote
        new_quote = '\n' + new_quote
        quotefile.write(new_quote)
    # print get_quote()

print get_quote()
