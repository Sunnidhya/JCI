# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 14:25:57 2019

@author: jroysu
"""

import csv
import math
#import numpy as np
FeatureVector = []
#Mean abnd Median Calculation and 1st and 3rd quartile calculation
with open('subrataDhanu-iOS.csv') as csf:
    csv_reader = csv.reader(csf,delimiter = ',')
    y = []
    z = []
    MedianX = []
    MedianY = []
    MedianZ = []
    sumX = 0.0
    sumY = 0.0
    sumZ = 0.0
    sumXavg = 0.0
    sumYavg = 0.0
    sumZavg = 0.0
    
    counter = 0
    for row in csv_reader:
        MedianX.append(float(row[0]))
        MedianY.append(float(row[1]))
        MedianZ.append(float(row[2]))
        counter = counter + 1
        sumX = sumX + float(row[0])
        sumY = sumY + float(row[1])
        sumZ = sumZ + float(row[2])
    sumXavg = sumX / counter
    sumYavg = sumY / counter
    sumZavg = sumZ / counter
#Standard Deviation and Variance Calculation
with open('subrataDhanu-iOS.csv') as csf:
    csv_reader = csv.reader(csf,delimiter = ',')
    sum1X = 0.0
    sum1Y = 0.0
    sum1Z = 0.0
    for row in csv_reader:
        sum1X = sum1X + ((float(row[0]) - sumXavg)**2)
        sum1Y = sum1Y + ((float(row[1]) - sumYavg)**2)
        sum1Z = sum1Z + ((float(row[2]) - sumZavg)**2)
    Vx = sum1X / counter
    Vy = sum1Y / counter
    Vz = sum1Z / counter
    SDx = math.sqrt(sum1X / counter)
    SDy = math.sqrt(sum1Y / counter)
    SDz = math.sqrt(sum1Z / counter)
FeatureVector.append(Vx)
FeatureVector.append(Vy)
FeatureVector.append(Vz)

print(FeatureVector)






    