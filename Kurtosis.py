# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 11:47:10 2019

@author: jroysu
"""

import csv
with open('prasanna to last cub alvina 5.csv') as csf:
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
    print(sumXavg,sumYavg,sumZavg)
    
with open('prasanna to last cub alvina 5.csv') as csf:
    csv_reader = csv.reader(csf,delimiter = ',')
    sumNumeratorX = 0.0
    sumNumeratorY = 0.0
    sumNumeratorZ = 0.0
    sumDenominatorX = 0.0
    sumDenominatorY = 0.0
    sumDenominatorZ = 0.0
    for row in csv_reader:
        sumNumeratorX = sumNumeratorX + (float(row[0]) - sumXavg)**4
        sumDenominatorX = sumDenominatorX + (float(row[0]) - sumXavg)**2
        sumNumeratorY = sumNumeratorY + (float(row[1]) - sumYavg)**4
        sumDenominatorY = sumDenominatorY + (float(row[1]) - sumYavg)**2
        sumNumeratorZ = sumNumeratorZ + (float(row[2]) - sumZavg)**4
        sumDenominatorZ = sumDenominatorZ + (float(row[2]) - sumZavg)**2
    Kx = sumNumeratorX /(sumDenominatorX**2)
    Ky = sumNumeratorY /(sumDenominatorY**2)
    Kz = sumNumeratorZ /(sumDenominatorZ**2)
print('Kurtosis values are Kx: {} Ky: {} Kz: {}'.format(Kx,Ky,Kz))
         
        
        
        
        
        
        
        
        
        