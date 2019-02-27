# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 15:18:08 2019

@author: jroysu
"""

import csv
import math
import numpy as np
from matplotlib import pyplot as plt
#with open('suyash390-389-iOS.csv') as csf:
#    csv_reader = csv.reader(csf,delimiter = ',')
#    y = []
#    z = []
#    counter = 0.0
#    for row in csv_reader:
#        y.append(math.sqrt((float(row[0])*float(row[0]))+(float(row[1])*float(row[1]))+(float(row[2])*float(row[2]))))
#        counter = counter+1
#        z.append(counter)    
#with open('Alvina-392-389-ios.csv') as csf:
#    csv_reader = csv.reader(csf,delimiter = ',')
#    y1 = []
#    z1 = []
#    counter1 = 0.0
#    for row in csv_reader:
#        y1.append(math.sqrt((float(row[0])*float(row[0]))+(float(row[1])*float(row[1]))+(float(row[2])*float(row[2]))))
#        counter1 = counter1+1
#        z1.append(float(counter1))  
#with open('390-388-hemant-iOS.csv') as csf:
#    csv_reader = csv.reader(csf,delimiter = ',')
#    y2 = []
#    z2 = []
#    counter2 = 0.0
#    for row in csv_reader:
#        y2.append(math.sqrt((float(row[0])*float(row[0]))+(float(row[1])*float(row[1]))+(float(row[2])*float(row[2]))))
#        counter2 = counter2 + 1
#        z2.append(counter2)    
with open('prasanna to last cub alvina ios-.csv') as csf:
    csv_reader = csv.reader(csf,delimiter = ',')
    y3 = []
    z3 = []
    counter3 = 0.0
    for row in csv_reader:
        y3.append(math.sqrt((float(row[3])*float(row[3]))+(float(row[4])*float(row[4]))+(float(row[5])*float(row[5]))))
        counter3 = counter3 + 1
        z3.append(counter3)  
    print(np.max(y3),np.min(y3))
    


#    plt.scatter(z,y,s=0.8,color ='r')
#    plt.scatter(z1,y1,s=0.8,color = 'g')
#    plt.scatter(z2,y2,s=0.8,color = 'k')
    plt.scatter(z3,y3,s=0.8,color = 'b')
    plt.xlabel('TimeStamp')
    plt.ylabel('Magnitude')
    plt.savefig('RangePlot7.png',dpi=300)