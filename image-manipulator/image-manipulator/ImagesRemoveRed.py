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

for i in range(0,x,1) :
    for j in range(0,y,1) :
        pixRGB = pix[i,j]
        imgarr[0] = 0;
        imgarr[1] = pixRGB[1];
        imgarr[2] = pixRGB[2];
        pix[i,j] = tuple(imgarr);
        #result = Image.fromarray((pix).astype(numpy.uint8))
im.save('D:/out2-red.jpg',"PNG")

