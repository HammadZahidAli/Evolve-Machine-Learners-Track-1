# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 19:05:39 2017

# Class 3 ASsignment
@author: Hammad Zahid
"""


# Equation of Line
# 3+5j

real=0
img=0


print('Enter Any Real Number: ')
a=(input(real))


print('Enter Any Imaginary Number:')
b = (input(img))


real = float(a)
img = float(b)

import cmath
#1 Angle of 3+5j
cmath.phase(complex(real, img))


#2 Returns Norms + Angle
norm, angle = cmath.polar(complex(real, img))



print('norm: ',norm)
print('angle:',angle)

