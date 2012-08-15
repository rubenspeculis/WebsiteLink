#!/usr/bin/env python

# get_links.py

import sys
import urllib
from urlparse import urlparse, urljoin
from BeautifulSoup import BeautifulSoup

def process(url):
    page = urllib.urlopen(url)
    
    text = page.read()
    page.close()

    soup = BeautifulSoup(text)
    netloc = urlparse(url)
    
    results = []

    for tag in soup.findAll('a', href=True):
        temp = urlparse(tag['href'])

        if temp.scheme != 'http':
            tag['href'] = urljoin(url, tag['href'])
            current = urlparse(tag['href'])
            if current.netloc == netloc.netloc:
                results.append(tag['href'])

    return results
# process(url)

def main():
    if len(sys.argv) == 1:
        print "Rubens' Link Extractor v0.2"
        print "Usage: %s URL [URL]..." % sys.argv[0]
        sys.exit(-1)

    # else, if at least one parameter was passed
    
    for url in sys.argv[1:]:
        a = process(url)
    
    for i in range(len(a)):
        print a[i]
        path = a[i]
        b = process(path)
        for k in range(len(b)):
            print '----' + b[k]
            path2 = b[k]
            c = process(path2)
            for m in range(len(c)):
               print '--------' + c[m]

# main()

if __name__ == "__main__":
    main()