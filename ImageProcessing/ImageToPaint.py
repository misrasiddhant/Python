# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 19:12:51 2019

@author: Siddhant
"""


from PIL import Image
#import math

im = Image.open("D:/Projects/bird.jpg") #Can be many different formats.
pix = im.convert('RGB')
print(im.size) #Get the width and hight of the image for iterating over
x = im.size[0]
y = im.size[1]

img_arr = []

for i in range(0,x,1) :
    for j in range(0,y,1) :
        img_arr.append(pix.getpixel((i,j)))
        
        
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=8)
kmeans.fit(list(set(img_arr)))
y_kmeans = kmeans.predict(img_arr)

centers = kmeans.cluster_centers_

int(centers[1][1])

indx=0
for i in range(0,x,1) :
    for j in range(0,y,1) :
        center=centers[y_kmeans[indx]]
        pix.putpixel((i,j),(int(center[0]),int(center[1]),int(center[2])))
        indx+=1

pix.save("D:/Projects/bird_new.png","PNG")
im.close()
