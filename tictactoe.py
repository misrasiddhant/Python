# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 01:29:24 2019

@author: Siddhant
"""

from sklearn import tree
import random
import time

def updateMatrix(a,val,pl):
    print(val)
    x=int(val.split(",")[0])
    y=int(val.split(",")[1])
    pos = x * 3 + y
    print(pos)
    
    if a[pos] != 0 or x > 2 or y > 2:
        print("Invalid Input")
        return 0
    a[pos]=pl
    return 1,a

def playRandomo(a,pl):
    openPosition = []
    for i in range(0,len(a)):
        if a[i] == 0:
            openPosition.append(i)    
    randIndex = random.randrange(0,len(openPosition))
    a[openPosition[randIndex]] = pl
    return 1,a

def playCognitive(a,pl):
    for event in X:
        for i in a:
            
 

def printGrid(a):
    zerocount = 0
    print("\n")
    for j in range(0,len(a)):
        if (j%3==0):
            print("\n", end= " ")
        print(str(a[j]).replace("0","-"), end= " ")
        if(a[j] == 0):
            zerocount = zerocount + 1
    print("\n")
    return zerocount    




def getNumericArray(NA):
    gridArray = []
    for e in NA:
        if(e == 0):
            gridArray.append(0)
        else:
            gridArray.append(int(e.replace("X","1").replace("O","2")))    
    return gridArray



    

def getArrayVector(A):
    index = 0
    vector = 0
    for e in A:
        vector = vector + e*pow(3,index)
        index = index + 1
    print(vector, A)
    return vector




def checkWin(a):
    zerocount = printGrid(a)
        
    # Horizontal and Vertical Events
    for i in range(0,3):
        if(a[0+(i*3)] == a[1+(i*3)] and a[0+(i*3)] == a[2+(i*3)] and a[0+(i*3)] != 0):
            print("Player %s wins" % str(a[0+(i*3)]) )
            return a[0+i]
        if(a[0+i] == a[3+i] and a[0+i]== a[6+i] and a[0+i] != 0):
            print("Player %s wins" % str(a[0+i]) )
            return a[0+i]
    
    if(a[0] == a [4] and a[0] == a [8] and a[0] !=0):
        print("Player %s wins" % str(a[0]) )
        return a[0+i]
    
    if(a[2] == a [4] and a[2] == a [6] and a[2] !=0):
        print("Player %s wins" % str(a[2]) )
        return a[0+i]
    
    if zerocount == 0:
        print("Draw")
        return 0
    return -1
    





def start():
    xgame = []
    a = [0,0,0,0,0,0,0,0,0]
    turn = 0
    while(True):
        # time.sleep(0.01)
        if(turn == 0):
            #v = input("Enter x,y : ")
            #feedback = updateMatrix(v,1)
            feedback,a = cpuplay(a,"X")
            turn = (turn + feedback)%2
        else:
            feedback,a = cpuplay(a,"O")
            turn = (turn + feedback)%2
        winner = checkWin(a)
       # X3D.append(getNumericArray(a))
        xgame.append(getArrayVector(getNumericArray(a)))
        if( winner != -1):
            xgame.extend([0]*(9-len(xgame)))
            return xgame,winner
    return xgame,0






########## MAIN ##################
#X3D = []
X = []
Y = []

for i in range(1,50):
    x,y = start()
    X.append(x)
    Y.append(y)





TrainY = []
for e in Y:
    if(e == 0):
        TrainY.append(0)
    else:
        TrainY.append(int(e.replace("X","1").replace("O","2")))    

dt = tree.DecisionTreeClassifier()
dt = dt.fit(X,TrainY)


import graphviz
dt_graph = tree.export_graphviz(dt)
graph = graphviz.Source(dt_graph)

graph.render("iris")
