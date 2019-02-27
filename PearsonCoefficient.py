# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 09:34:45 2019

@author: jroysu
"""
import csv
import math
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
    
with open('390-lowest-iOS.csv') as csf1:
    csv_reader1 = csv.reader(csf1,delimiter = ',')
    sumXsquare = 0.0
    sumYsquare = 0.0
    sumZsquare = 0.0
    
    sumNumerator = 0.0
    sumDenominator = 0.0
    for row in csv_reader1:
        sumNumerator = sumNumerator + ((float(row[0]) - sumXavg)*(float(row[1]) - sumYavg)*(float(row[2]) - sumZavg))
        sumXsquare = sumXsquare + (float(row[0]) - sumXavg)*(float(row[0]) - sumXavg)
        sumYsquare = sumYsquare + (float(row[1]) - sumYavg)*(float(row[1]) - sumYavg)
        sumZsquare = sumZsquare + (float(row[2]) - sumZavg)*(float(row[2]) - sumZavg)
        
    sumDenominator = math.sqrt(sumXsquare)*math.sqrt(sumYsquare)*math.sqrt(sumZsquare)
    PearsonCoefficient = math.sqrt((sumNumerator / sumDenominator)*(sumNumerator / sumDenominator))
    print(PearsonCoefficient)
       