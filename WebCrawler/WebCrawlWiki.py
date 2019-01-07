# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 13:55:14 2017

@author: Siddhant Misra
"""

website_base_url = 'https://en.wikipedia.org/'

url_extn = 'wiki/List_of_Bollywood_films_of_2016'

movielist = []


import urllib2
response = urllib2.urlopen('https://en.wikipedia.org/wiki/List_of_Bollywood_films_of_2016')
html = response.read()
table_elements = html.replace('\n','').split('<table class="wikitable sortable">')

#itms = table_elements[1].replace('<i>',',"').replace('<td>','').replace('</td>','","').replace('<th>','').replace('</th>','","').split('</tr><tr>')
itms = table_elements[1].split('</tr><tr>')
attr = itms[1].split('</td>')

import re

for i in itms:
    attr = i.split('</td>')
    movie = []
    for a in reversed(attr):
        movie.append(re.sub("<.*?>", " ", a).strip())
    movielist.append(movie)




f = open('D:/myfile.csv', 'w')
for i in itms:
    f.write(re.sub("<.*?>", " ", i))
    f.write('\n')
f.close()  