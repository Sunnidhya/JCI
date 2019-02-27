# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 18:16:24 2019

@author: jroysu
"""
import csv
import numpy as np
with open('389-xMagNorthZVertical-iOS.csv') as csf:
    csv_reader = csv.reader(csf,delimiter=',')
    xi = []
    yi = []
    zi = []
    counter = 0
    for row in csv_reader:
        xi.append(float(row[0]))
        yi.append(float(row[1]))
        zi.append(float(row[2]))
        counter = counter + 1
with open('alvina.csv') as csf:
    csv_reader = csv.reader(csf,delimiter=',')
    xa = []
    ya = []
    za = []
    for row in csv_reader:
        xa.append(float(row[0]))
        ya.append(float(row[1]))
        za.append(float(row[2]))
xdiv = []
ydiv = []
zdiv = []
for i in range(counter):
    xdiv.append(xi[i] / xa[i])
    ydiv.append(yi[i] / ya[i])
    zdiv.append(zi[i] / za[i])
print(np.mean(xdiv),np.mean(ydiv),np.mean(zdiv))
    
    

