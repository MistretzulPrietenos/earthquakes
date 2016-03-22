import re
import socket
import urllib2
from BeautifulSoup import BeautifulSoup
from BeautifulSoup import BeautifulStoneSoup

# number of seconds to wait before trying to load the webpage again
socket.setdefaulttimeout(10)

# number of failures to wait before giving up on a page
FAILS = 100

def mysoupopen(url):
    loaded = False
    ret = None
    fails = 0
    while(not loaded):
        try:
	    # modified beautiful soup to evaluate html entities
	    ret=BeautifulStoneSoup(urllib2.urlopen(url), 
                   convertEntities=BeautifulStoneSoup.HTML_ENTITIES)
            loaded = True
        except:
            fails += 1
        if(fails > FAILS):
            break;
    return ret

def cleanhtml(str):
    str = str.replace("&quot;","\""); # &quot; -> "
    str = str.replace("&#174;",""); # registered trademark symbol
    str = str.replace("&amp;","&"); # &amp; -> &
    str = str.replace("&#34;","\""); # &#34; -> "
    return str;
