# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 13:55:14 2017

@author: Siddhant Misra
"""

import re
import urllib
from bs4 import BeautifulSoup

def get_syllable(url):
    #url = 'http://www.syllablecount.com/syllables/naval'
    try:
        print(url)
        url_response = urllib.request.urlopen(url)
        url_document = url_response.read()
        url_soup = BeautifulSoup(url_document, 'html.parser')
        return(url_soup.find("p", {"id": "ctl00_ContentPane_paragraphtext2"}).find("b").text)
    except:
        return ""


website_base_url = 'http://www.syllablecount.com'


get_syllable('http://www.syllablecount.com/syllables/naval')


response = urllib.request.urlopen('http://www.syllablecount.com/syllables/words/')
html = response.read()
html_doc  = 'http://www.syllablecount.com/syllables/words/'
soup = BeautifulSoup(html, 'html.parser').find("table",{"id":"ctl00_ContentPane_DataList3"})

print(soup.title)
soup.prettify()
soup.find_all('a')

lst = []

for link in soup.find_all('a'):
    if(re.search("/syllables/[a-z]",link.get('href')) != None):
        syll = get_syllable(website_base_url+link.get('href'))
        print(syll)
        lst.append(syll)
    


#itms = table_elements[1].replace('<i>',',"').replace('<td>','').replace('</td>','","').replace('<th>','').replace('</th>','","').split('</tr><tr>')
itms = table_elements[1].split('</tr><tr>')
attr = itms[1].split('</td>')

soup.a

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