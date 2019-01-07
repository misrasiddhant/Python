# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 21:02:56 2018

@author: Siddhant
"""
import re

import urllib
from bs4 import BeautifulSoup

sentence="""Israeli Prime Minister Benjamin Netanyahu’s government agreed Monday to hold early elections in April after the ruling coalition appeared to come up short on votes needed to pass a contentious piece of court-ordered legislation."
Netanyahu said his coalition “unanimously” agreed to disband the government and hold a new election. At a meeting of his Likud faction, he listed his accomplishments in office and said he hoped his current religious, nationalistic coalition would be the “core” of the next one as well."
"“We will ask the voters for a clear mandate to continue leading the state of Israel our way,” he said to applause from party members."
"The Knesset, or parliament, is expected to hold a vote on Wednesday to formally dissolve, setting the stage for a three-month election campaign and a likely vote on April 9."""


##### Cleanup #####
sentence=re.sub("[^A-Za-z\s]+","",sentence).replace("\n"," ")
words = sentence.split(" ");



def get_word_type(word):
    """Function defined to get all the product details"""
    try:
        url="https://www.dictionary.com/browse/"+word.lower()
        response = urllib.request.urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        soup.prettify()
        word_type = "\""+soup.find("span",{"class":"luna-pos"}).text.strip()+"\""
    except:
        word_type = "unknown"
    return word_type

word_dict={}

type(word_dict.keys)
for word in words:
    if word not in word_dict.keys():
        word_dict[word]=get_word_type(word)
    