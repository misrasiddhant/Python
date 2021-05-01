# -*- coding: utf-8 -*-
"""
Created on Sun May 07 17:02:11 2017

@author: Siddhant Misra
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 10:34:27 2017

@author: Siddhant Misra
"""

from PIL import Image
#import math

im = Image.open("D:/test 2.jpg") #Can be many different formats.
pix = im.load()
print im.size #Get the width and hight of the image for iterating over
x = im.size[0]
y = im.size[1]

white = [255,255,255]
red = [255,0,0]     
orange = [255,128,0]
yellow = [255,255,0]
limeGreen = [128,255,0]       
green = [0,255,0]
kiwiGreen = [0,255,128]            
cyan = [0,128,128]
ltBlue = [0,128,255]           
blue = [0,0,255]            
purple = [128,0,255]            
pink = [255,0,255] 
magenta = [255,0,128]      
navy = [0,0,128]      
black = [0,0,0]            
#colorArr = [white,red,orange,yellow,limeGreen,green,kiwiGreen,cyan,ltBlue,blue,purple,pink,magenta,navy,black]
colorArr = [[0,0,0],[128,0,85],[255,0,170],
            [0,128,255],[128,128,255],[255,128,0],
            [0,255,64],[128,255,128],[255,255,192],
            [0,0,255],[128,0,0],[255,0,64],
            [0,128,128],[128,128,192],[255,128,255],
            [0,255,0],[128,255,64],[255,255,128],
            [0,0,192],[128,0,255],[255,0,0],
            [0,128,64],[128,128,128],[255,128,192],
            [0,255,255],[128,255,0],[255,255,64]]
z = len(colorArr)

threshold = 60

for i in range(0,x,1) :
    for j in range(0,y,1) :
        pixRGB = pix[i,j]
        sumWRGBB = [0] * z
        #sumWRGBB = [0,0,0,0,0,0,0,0,0,0,0,0,0,0] ;
        #print(len(sumWRGBB))
        for k in range (0,3,1) :
            for l in range (0,z,1) :
                sumWRGBB[l] += (colorArr[l][k]-pixRGB[k])*(colorArr[l][k]-pixRGB[k])
                        
        minRGB = min(sumWRGBB)
        for l in range (0,z,1) :
            if minRGB == sumWRGBB[l] :
                pix[i,j] = tuple(colorArr[l])
        
        #result = Image.fromarray((pix).astype(numpy.uint8))
im.save('D:/out2.jpg',"PNG")

