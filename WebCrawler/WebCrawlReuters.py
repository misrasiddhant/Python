# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 13:55:14 2017

@author: Siddhant Misra
"""
 


get_news_contents("https://in.reuters.com/article/india-energy-biofuels-idINKBN1AQ0ZU")


latest_headlines = get_links(website_base_url+link.get('href'), "div", "latestHeadlines")




    
    link.text.strip()
    
    print(link.get('href') +":"+ link.text.strip())
    

for link in news_link :
    if(re.search("/article/",link.get('href')) != None):
        print(link.get('href') +":"+ link.text.strip())
    else:
        get_archive_links(link,website_base_url)

news_link2 = get_links("https://in.reuters.com/news/technology", "div", "moreSectionNews")
for link in news_link2 :
    if(re.search("/article/",link.get('href')) != None):
        print(link.get('href') +":"+ link.text.strip())


f = open('D:/myfile.csv', 'w')
for i in itms:
    f.write(re.sub("<.*?>", " ", i))
    f.write('\n')
f.close()  