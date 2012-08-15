#!/usr/bin/env python

# get_links.py

import re
import sys
import urllib
from urlparse import urlparse, urljoin
from BeautifulSoup import BeautifulSoup

class MyOpener(urllib.FancyURLopener):
    version = 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15'

def process(url):
    page = urllib.urlopen(url)
    
    text = page.read()
    page.close()

    soup = BeautifulSoup(text)

    results = []

    for tag in soup.findAll('a', href=True):
        temp = urlparse(tag['href'])
        if temp.scheme != 'http':
            tag['href'] = urljoin(url, tag['href'])
            results.append(tag['href'])

    return results
# process(url)

def main():
    if len(sys.argv) == 1:
        print "Jabba's Link Extractor v0.1"
        print "Usage: %s URL [URL]..." % sys.argv[0]
        sys.exit(-1)


    # else, if at least one parameter was passed
    
    for url in sys.argv[1:]:
        a = process(url)
    
    for i in range(len(a)):
        print a[i]
        path = a[i]
        if a[i] != 'mailto:contactus@myregion.gov.au':
            b = process(path)
            for k in range(len(b)):
                print '----' + b[k]
                path2 = b[k]
                if b[k] != 'mailto:contactus@myregion.gov.au':
                    c = process(path2)
                    for m in range(len(c)):
                        print '--------' + c[m]

# main()

if __name__ == "__main__":
    main()