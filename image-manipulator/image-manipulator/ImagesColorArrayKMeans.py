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

import random
from math import sqrt

from PIL import Image

#import math


def col_distance(point1, point2):
    """ Calculates distance btw 2 pints"""
    sum = 0
    for i in range(0,len(point1)):
        sum = sum + ((point1[i]-point2[i])**2)
    
    return sqrt(sum)    


im = Image.open("D:/test 2.jpg") #Can be many different formats.
pix = im.load()
print im.size #Get the width and hight of the image for iterating over
x = im.size[0]
y = im.size[1]

k_value = 30

rand_points_x = random.sample(range(1,x),k_value)
rand_points_y = random.sample(range(1,y),k_value)

for i in range(0,x,1) :
    for j in range(0,y,1) :
        
        pixRGB = pix[i,j]
        min_dist = col_distance(pixRGB, pix[rand_points_x[0],rand_points_y[0]])
        for k in range(1,k_value):
            dist = col_distance(pixRGB, pix[rand_points_x[k],rand_points_y[k]])
            if dist < min_dist:
                pix[i,j] = pix[rand_points_x[k],rand_points_y[k]]
                min_dist = dist
         #result = Image.fromarray((pix).astype(numpy.uint8))
im.save('D:/out2.jpg',"PNG")
