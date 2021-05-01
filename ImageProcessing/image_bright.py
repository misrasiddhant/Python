# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 17:43:29 2017

@author: Siddhant Misra
@program : Impage Processing
"""



def img_brightness(pixel):
    """Takes the pixel as in input which is an array of the form [R,G,B]
    and returns the calculated brightness which a floating point number"""
    R = pixel[0]
    G = pixel[1]
    B = pixel[2]
    return(0.2126*R + 0.7152*G + 0.0722*B)
    
def img_rgb_ratio(pixel):
    """ Takes pixel as an input of type array and returns the ratio of r g and b values"""
    total = sum(pixel)
    pixel_ratio = []
    if(total>0):
        Rr = pixel[0]/total
        Gr = pixel[1]/total
        Br = pixel[2]/total
        pixel_ratio.append(Rr)
        pixel_ratio.append(Gr)
        pixel_ratio.append(Br)
    else:
        pixel_ratio.append(0)
        pixel_ratio.append(0)
        pixel_ratio.append(0)
    return pixel_ratio
    
def new_pixel (pixel_ratio, brightness):
    Rr = pixel_ratio[0]
    Gr = pixel_ratio[1]
    Br = pixel_ratio[2]
    
    total = brightness - (Rr+Gr+Br)
    pixel=[int(Rr*total), int(Gr * total), int(Br * total)]
    return tuple(pixel)
    
from PIL import Image
#import math

im = Image.open("D:/test 2.jpg") #Can be many different formats.
pix = im.load()
x = im.size[0]
y = im.size[1]

for i in range(0,x,1) :
    for j in range(0,y,1) :
        pixRGB = pix[i,j]
        pix_r = img_rgb_ratio(pixRGB)
        bright = img_brightness(pixRGB)
        bright = bright + (0.40*bright)
        #print(bright)
        p = new_pixel(pix_r, bright)
        #print(p[0])
        pix[i,j]  = p
        #result = Image.fromarray((pix).astype(numpy.uint8))
im.save('D:/out2-bright.jpg',"PNG")

 