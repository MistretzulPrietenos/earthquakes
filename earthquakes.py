#!/bin/env python
import sys
import urllib2
from BeautifulSoup import *

FILE='earthquakes.tsv'

def scrape_data():
    page = urllib2.urlopen("http://www.ngdc.noaa.gov/nndc/struts/results?bt_0=1900&st_0=2007&type_17=Or&query_17=None+Selected&type_12=EXACT&query_12=&type_12=Or&query_14=None+Selected&type_3=Like&query_3=&st_1=&bt_2=&st_2=&bt_1=&bt_4=5&st_4=&bt_5=&st_5=&bt_6=&st_6=&bt_7=&st_7=&bt_8=&st_8=&bt_9=&st_9=&bt_10=&st_10=&type_11=Exact&query_11=&type_16=Exact&query_16=&display_look=1&t=101650&s=1&submit_all=Search+Database")
    print "Initializing beautiful soup."
    soup = BeautifulSoup(page)
    fd = open(FILE, 'w')
    print "Parsing HTML content."

    delim = '\t'
    indices = [0, 1, 2, 9, 10, 11, 12, 13, 14, 15]
    earthquakes = soup.findAll('tr', attrs={'valign' : 'top'})
    item_count = 1
    print("Writing to file %s" % FILE)
    for quake in earthquakes[1:]:
        sys.stdout.flush()
        quake_tds = quake.findAll('td')
        for i in range(0, len(indices)):
            contents = quake_tds[indices[i]].contents
            if len(contents) != 0:
                fd.write(str(contents[0]).strip()),
            if i != len(indices) -1:
                fd.write(delim),
        fd.write('\n'),
        fd.flush()
        item_count += 1
    print "----------- processed %d items.", (item_count -1)
    fd.close()

if __name__ == "__main__":
    scrape_data()

