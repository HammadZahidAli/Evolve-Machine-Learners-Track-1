# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 21:12:57 2017

@author: Hammad Zahid



These are some functions implementation related to vectors
Currently simple 1D vector like [1,2]
"""

# enter ctrl + i to explore about math module
import math
import numpy as np



def add(v1, v2):
   result = []

   # To get length of vector use len method
   for i in range(len(v1)):
       result.append(v1[i] + v2[i])

   return result



def sub(v1, v2):
   result = []

   for i in range(len(v1)):
       result.append(v1[i] - v2[i])

   return result




def dot(v1, v2):
   result = 0
   
   print("Dot product ",np.dot(np.array(v1),np.array(v2)))
   
   for i in range(len(v1)):
       result= result + (v1[i] * v2[i])
      

   return result




def magnitude(v1):
    # print("norm or magnitude:",np.linalg.norm(v1))
    return round(math.sqrt(math.pow(v1[0],2)+math.pow(v1[1],2)),2)
    
    

def unitVector(v):
    # print(np.array([1,2])/magnitude(v))
    return ([round((x / magnitude(v)),2) for x in v])

# Sample Vectors
a = [1, 2]
b = [2, 2]

print("Addition: ", add(a, b))
print("Subtraction: ", sub(a, b))
print("Dot: ", dot(a, b))

print("Magnitude: ",magnitude(a))
print("Unit of ",a ," is",unitVector(a))