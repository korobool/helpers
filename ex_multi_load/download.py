#!/usr/bin/python

import os
import re

__author__ = 'oleksandr'

import sys
import httplib, urllib

site = 'www.ex.ua'

page_link = sys.argv[1]

conn = httplib.HTTPConnection(site)

conn.request("GET", page_link)
response = conn.getresponse()
print response.status, response.reason


page_html = response.read()

#print page_html

pattern = "(?<=href=')/get/[\d]+"

matches = re.finditer(pattern, page_html)

download_links = sorted(list(set(map(lambda m: site + m.group(0), matches))))

def process_download_link(lnk):
    os.system('wget --content-disposition --restrict-file-names=nocontrol -c ' + lnk)
    # Alternative way (might be better) 
    # "curl -O " + lnk

for lnk in download_links:
    process_download_link(lnk)



