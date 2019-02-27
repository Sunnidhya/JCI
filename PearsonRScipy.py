# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 16:08:54 2019

@author: jroysu
"""

import csv
import math
from scipy.stats import pearsonr as pr

with open('prasanna to last cub alvina 5.csv') as csf:
    csv_reader = csv.reader(csf,delimiter=',')
    x = []
    y = []
    z = []
    total = []
    for row in csv_reader:
        x.append(float(row[0]))
        y.append(float(row[1]))
        z.append(float(row[2]))        
        total.append(math.sqrt((float(row[0])**2)+(float(row[1])**2)+(float(row[2])**2)))
with open('prasanna to last cub alvina 3.csv') as csf:
    csv_reader = csv.reader(csf,delimiter=',')
    x1 = []
    y1 = []
    z1 = []
    total1 = []
    for row in csv_reader:
        x1.append(float(row[0]))
        y1.append(float(row[1]))
        z1.append(float(row[2]))        
        total1.append(math.sqrt((float(row[0])**2)+(float(row[1])**2)+(float(row[2])**2)))
print(pr(x,x1))
print(pr(y,y1))
print(pr(z,z1))
print(pr(total,total1))