# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 10:34:27 2017

@author: Siddhant Misra
"""

import math

from PIL import Image

im = Image.open("D:/test.jpg") #Can be many different formats.
pix = im.load()
print im.size #Get the width and hight of the image for iterating over
x = im.size[0]
y = im.size[1]

white = [255,255,255]
threshold = 60
colorArr = []
#colorArr.append([])

for i in range(0,x,1) :
    for j in range(0,y,1) :
        pixRGB = pix[i,j]
        sum = 0
        #print(type(pixRGB))
        for k in range (0,3,1) :
            #print((white[k]-pixRGB[k]))
            sum += (white[k]-pixRGB[k])*(white[k]-pixRGB[k])
        #print(math.sqrt(sum))
        if math.sqrt(sum) < threshold :
            pix[i,j] = tuple(white)
            
red = [255,0,0]            
for i in range(0,x,1) :
    for j in range(0,y,1) :
        pixRGB = pix[i,j]
        sum = 0
        for k in range (0,3,1) :
            sum += (red[k]-pixRGB[k])*(red[k]-pixRGB[k])
        if math.sqrt(sum) < threshold :
            pix[i,j] = tuple(red)
            
green = [0,255,0]            
for i in range(0,x,1) :
    for j in range(0,y,1) :
        pixRGB = pix[i,j]
        sum = 0
        for k in range (0,3,1) :
            sum += (green[k]-pixRGB[k])*(green[k]-pixRGB[k])
        if math.sqrt(sum) < threshold :
            pix[i,j] = tuple(green)


blue = [0,0,255]            
for i in range(0,x,1) :
    for j in range(0,y,1) :
        pixRGB = pix[i,j]
        sum = 0
        for k in range (0,3,1) :
            sum += (blue[k]-pixRGB[k])*(blue[k]-pixRGB[k])
        if math.sqrt(sum) < threshold :
            pix[i,j] = tuple(blue)
            
            
black = [0,0,0]            
for i in range(0,x,1) :
    for j in range(0,y,1) :
        pixRGB = pix[i,j]
        sum = 0
        for k in range (0,3,1) :
            sum += (black[k]-pixRGB[k])*(black[k]-pixRGB[k])
        if math.sqrt(sum) < threshold :
            pix[i,j] = tuple(black)            
            
#result = Image.fromarray((pix).astype(numpy.uint8))
im.save('D:/out.jpg',"PNG")

