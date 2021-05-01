# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 10:34:27 2017

@author: Siddhant Misra
"""

from PIL import Image

im = Image.open("D:/rumors.jpg") #Can be many different formats.
pix = im.load()
print im.size #Get the width and hight of the image for iterating over
x = im.size[0]
y = im.size[1]


colorArr = []
#colorArr.append([])

for i in range(0,x,1) :
    for j in range(0,y,1) :
        flg = 0
        if len(colorArr) > 0:
            for indx in range(0,len(colorArr)):
                if pix[i,j] == colorArr[indx][0] :
                    colorArr[indx][1] = colorArr[indx][1] + 1
                    flg=1
        
            if flg == 0:
                colorArr.append([])
                colorArr[len(colorArr)-1].append(pix[i,j])
                colorArr[len(colorArr)-1].append(1)
        else:
                colorArr.append([])
                colorArr[0].append(pix[i,j])
                colorArr[0].append(1)

        
for row in colorArr:
        print(row)
        
