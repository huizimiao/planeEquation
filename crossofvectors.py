#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 18:01:03 2018

@author: mayank
"""

p1=list((float(input('x1=')), float(input('y1=')), float(input('z1='))))
p2=list((float(input('x2=')), float(input('y2=')), float(input('z2='))))
p3=list((float(input('x3=')), float(input('y3=')), float(input('z3='))))

v1= list(((float(p1[0]-p2[0])),(float(p1[1]-p2[1])) ,(float(p1[2]-p2[2]))))
v2= list(((float(p1[0]-p3[0])),(float(p1[1]-p3[1])) ,(float(p1[2]-p3[2]))))
print (v1,v2)
import numpy as np
x= np.cross(v1,v2)
print (x)