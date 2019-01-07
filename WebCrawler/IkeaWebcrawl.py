# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 23:49:59 2018

@author: Siddhant Misra
"""

website_base_url = 'https://www.ikea.com/ca/en/'

linklist = []
urls = []
url_visited = []

import urllib
from bs4 import BeautifulSoup

def get_product(url):
    """Function defined to get all the product details"""
    try:
        response = urllib.request.urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        soup.prettify()
        productName = "\""+soup.find("span",{"class":"productName"}).text.strip()+"\""
        productType = "\""+soup.find("span",{"class":"productType"}).text.strip()+"\""
        packagePrice = soup.find("span",{"class":"packagePrice"}).text.strip()
        return (productName,productType,packagePrice)
    except:
        return ("","","")

def get_links(url):
    """Function defined to get all the links within an HTML container (div/nav) with the ID as container_id"""
    try:
        response = urllib.request.urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        soup.prettify()
        linklist = soup.find_all('a')
        for link in linklist:
                link = link.get('href')
                try:
                        if "/" in link:
                                if "http" in link:
                                        if link not in urls:
                                                urls.append(link)
                                else:
                                        if "https://www.ikea.com"+link not in urls:
                                                urls.append("https://www.ikea.com"+link)
                except:
                        continue
    except:
        return ""


get_links(website_base_url)
#==============================================================================
# 
# s = "https://www.iea.com/ms/en_CA/pdf/buying_guides/FY19/Workchairs_buying_guide_FY19"
# if s.find(".pdf")+s.find("www.ikea.com")>=-1:
#         print("not in")
# else:
#         print("in")
#==============================================================================

s = "https://www.ikea.com/ca/en/catalog/products/90271544/"
pd = get_product(s)
print(type(pd))
file= open("D:\ikea.txt",'w')
file.write(','.join(str(i) for i in pd)+"\n")
file.close()

file= open("D:\ikea.txt",'w')
for u in urls:
        if u.find(".pdf") ==-1 and u.find("www.ikea.com")!=-1:
                if u not in url_visited:
                        #print("Reading URL" + u)
                        get_links(u)
                        #file.write(u)
                        url_visited.append(u)
                        if u.find("/catalog/products/") != -1:
                                pd = get_product(u)
                                print(pd)
                                file.write(','.join(str(i) for i in pd)+"\n")
file.close()