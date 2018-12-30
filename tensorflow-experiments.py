# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 17:51:28 2017

@author: Siddhant Misra
"""

import tensorflow as tf
"""
a = tf.constant(3.0)
b= tf.constant(4.0, dtype = tf.float32)
print(a,b)

session = tf.Session()
session.run([a,b])

sum =  tf.add(a,b)
print(sum)

session.run(sum)

a = tf.placeholder(dtype = tf.float32)
b = tf.placeholder(dtype = tf.float32)
c = tf.add(a,b)

session.run(c,{a:2,b:5})
session.run(c,{a:[2,4],b:[5,9]})
session.run(c,{a:[[2,4],[3,5]],b:[[2,3],[5,9]]})
"""
session = tf.Session()

m = tf.Variable([.3], dtype = tf.float32)
c = tf.Variable([-.3], dtype = tf.float32)
x = tf.placeholder(dtype = tf.float32)
y = tf.placeholder(dtype = tf.float32)

linear_model = m*x+c

init= tf.global_variables_initializer()
session.run(init)
session.run(linear_model, {x:[1,2,3,4,5]})

SqErr = tf.squared_difference(linear_model ,y)
loss = tf.reduce_sum(SqErr)
    
session.run(loss,{x:[1,2,3,4,5],y:[2,6,10,14,18]})


print(loss)
optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(loss)

session.run(init)
for i in range(100000):
    session.run(train,{x:[1,2,3,4,5],y:[2,6,10,14,18]})
    
session.run([m,c])
session.run(loss,{x:[1,2,3,4,5],y:[2,6,10,14,18]})