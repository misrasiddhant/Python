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

imgarr = [0,0,0]

for i in range(0,x-1,1) :
    for j in range(0,y-1,1) :
        pix11 = pix[i,j]
        pix12 = pix[i,j+1]
        pix21 = pix[i+1,j]
        pix22 = pix[i+1,j+1]
        imgarr[0] = (pix11[0]+pix12[0]+pix21[0]+pix22[0])/4;
        imgarr[1] = (pix11[1]+pix12[1]+pix21[1]+pix22[1])/4;
        imgarr[2] = (pix11[2]+pix12[2]+pix21[2]+pix22[2])/4;
        pix[i,j] = tuple(imgarr);
        pix[i,j+1] = tuple(imgarr);
        pix[i+1,j] = tuple(imgarr);
        pix[i+1,j+1] = tuple(imgarr);
        #result = Image.fromarray((pix).astype(numpy.uint8))
im.save('D:/out2avg.jpg',"PNG")

