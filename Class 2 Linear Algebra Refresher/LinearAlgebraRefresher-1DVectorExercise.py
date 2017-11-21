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
   result = np.dot(np.array(v1),np.array(v2))
   return result




def magnitude(v1):
    return np.linalg.norm(v1)
    # [a**2 for a in v1]
    # print("norm or magnitude:",np.linalg.norm(v1))
    #return round(math.sqrt(math.pow(v1[0],2)+math.pow(v1[1],2)),2)
    
    

def unitVector(v):
    return [(x / magnitude(v)) for x in v]
    # print(np.array([1,2])/magnitude(v))
    #return ([round((x / magnitude(v)),2) for x in v])



def angle_between(a,b):
    a = unitVector(a)
    a= np.array(a)
    b = unitVector(b)
    b=np.array(b)
    angle = math.acos(np.dot(a,b)) * 180. /math.pi
    return angle


def parallel(a,b):
    print("Angle:",round(angle_between(a,b)))
    if(angle_between(a,b)==0 or round(angle_between(a,b))==180):
        print(a,"and",b,"are","parallel vectors")
    else:
        print("Not parallel")


def Orthogonal(a,b):
     print("Dot is",round(dot(a,b)))
     if(round(dot(a,b))==0):
        print(a,"and",b,"are","Orthogonal vectors")
     else:
        print("Not orthogonal")
        
    

# Sample Vectors
a1=[-2.328,-7.284,-1.214]
a2=[-1.821,1.072,-2.94]
m = [7.887,4.138]
g = [-8.802,6.776]
p=[3.1,-7.6]
k=[-2.6,5.3]
d,q=[0,1],[1,0]
h1=[-7.579,-7.88]
h2=[22.737,23.64]
b1=[-1,-1]
b2=[1,1]
Orthogonal(a1,a2)
Orthogonal([0,0],[0,0])
parallel(h1,h2)
print(dot(m,g))
print(angle_between(p,k))
a = [-0.221, 7.437]
b = [2, 2]

print("Addition: ", add(a, b))
print("Subtraction: ", sub(a, b))
print("Dot: ", dot(a, b))

# for n V
c= [1,2,3,3,44,4,]
print("Magnitude of: ",a," is ",magnitude(a))
print("Unit of ",c ," is\n",unitVector([1,2,3,3,44,4,]))