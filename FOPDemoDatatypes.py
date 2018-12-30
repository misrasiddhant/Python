# -*- coding: utf-8 -*-
"""
Created on Tue Jan 03 10:37:36 2017

@author: Aegis_1
"""

x=10
type(x)
y=12.5
type(y)
z="sachin"
type(z)

#1
age=18
if age>=18:
    print "eligible for vote"
else:
    print "not eligible for vote"
    
    
#2 Even or odd 
a=input("enter any no")    
if a%2==0:
    print "even no"
else:
    print "odd no"
    
#3 Reverse no
num=input("Enter any no")
rev=0
while num>0:
    d=num%10
    rev=rev*10+d
    num=num/10
print "reverse no is",rev

#Prime
i=2
n=input("Enter any number")
while n%i!=0:
    i=i+1
if n==i:
    print "prime"
else:
    print "not prime"
    
#4Armstrong num
num=input("Enter any no")
x=num
arm=0
while num>0:
    d=num%10
    arm=arm+d*d*d
    num=num/10
if x==arm:
    print "Armstrong  no is",x
else:
    print "Not Armstrong",x
    
 #1 for loop
n=[1,2,3,4,5]
for num in n:
    print num**2
    
#2

for i in range(1,10,2):
    print i
#Array    
import numpy as np
a=np.array([[1,2,3],[2,3,3],[1,1,1]])
b=np.array([[1,2,3],[2,3,3],[1,1,1]])
a+b
a
a[0]
a[:,2]
a[1,:]
#String 
s="   hello good   morning   "
s.upper()
s.lower()
s.strip()
s.split()
s.replace('good','1')
s.endswith("hi")


#dicttinary(Structure)
dict={'name':'sachin','age':7,'Qua':'ME' }
dict['name']

#list
l=[1,2,3,34,54]
l[2]=12
l

#tuple
t=1,2,3,4,5
t
t[2]=4

#Write the code to add 2 string in 2 different ways? 
a="hello"
b="good"
c=a+b
c
''.join([a,b])

#fibonacci
a=0
b=1
n=12
t=0
print a
print b
while t<=n:
    t=a+b
    print t
    a=b
    b=t

#factorial
n = input("Enter a number: ")
fact = 1
# check if the number is negative, positive or zero
if n < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif n== 0:
   print("The factorial of 0 is 1")
else:
    while n>0:
        fact=fact*n
        n=n-1
print("The factorial of number is",fact)



def dogno(x):
    abc = x.count("dog")
    print abc
dogno("This dog runs faster than the other dog dude!")