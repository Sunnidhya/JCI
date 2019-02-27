# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 11:47:10 2019

@author: jroysu
"""

import csv
with open('390-lowest-iOS.csv') as csf:
    csv_reader = csv.reader(csf,delimiter = ',')
    y = []
    z = []
    sumX = 0.0
    sumY = 0.0
    sumZ = 0.0
    sumXavg = 0.0
    sumYavg = 0.0
    sumZavg = 0.0
    
    counter = 0
    for row in csv_reader:
        counter = counter + 1
        sumX = sumX + float(row[0])
        sumY = sumY + float(row[1])
        sumZ = sumZ + float(row[2])
    sumXavg = sumX / counter
    sumYavg = sumY / counter
    sumZavg = sumZ / counter
    
with open('390-lowest-iOS.csv') as csf:
    csv_reader = csv.reader(csf,delimiter = ',')
    sumNumeratorX = 0.0
    sumNumeratorY = 0.0
    sumNumeratorZ = 0.0
    for row in csv_reader:
        sumNumeratorX = sumNumeratorX + (row[0] - sumXavg)**4
        sumNumeratorY = sumNumeratorY + (row[1] - sumYavg)**4
        sumNumeratorZ = sumNumeratorZ + (row[2] - sumZavg)**4