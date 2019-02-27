# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 12:22:17 2019

@author: jroysu
"""

import csv
import math
from matplotlib import pyplot as plt
# Mean Calculation
with open('378A.csv') as csf:
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
        y.append(counter)
        sumX = sumX + float(row[0])
        sumY = sumY + float(row[1])
        sumZ = sumZ + float(row[2])
    sumXavg = sumX / counter
    sumYavg = sumY / counter
    sumZavg = sumZ / counter
#Standard Deviation and Variation Calculation
with open('378A.csv') as csf:
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
    print(SDx,SDy,SDz)
    print(Vx,Vy,Vz)
    
#Calculating Coefficient of Variation and Inverse of Coefficient of Variation
CVx = (SDx / sumXavg) * 100
CVy = (SDy / sumYavg) * 100
CVz = (SDz / sumZavg) * 100
print(CVx,CVy,CVz)

ICVx = 1/CVx
ICVy = 1/CVy
ICVz = 1/CVz

print(ICVx,ICVy,ICVz)
##Signature Normalization-Normalised X,Y,Z
with open('378A.csv') as csf:
    csv_reader = csv.reader(csf,delimiter = ',')
    Nx = []
    Ny = []
    Nz = []
    for row in csv_reader:
        Nx.append((math.sqrt(((float(row[0])-sumXavg)/SDx)**2)))
        Ny.append((math.sqrt(((float(row[1])-sumYavg)/SDy)**2)))
        Nz.append((math.sqrt(((float(row[2])-sumZavg)/SDz)**2)))
        
plt.subplot(2,2,1)
plt.scatter(y,Nx,s=0.3)
plt.xlabel('TimeStamp')
plt.ylabel('Normalised Magnitude X')
plt.subplot(2,2,2)
plt.scatter(y,Ny,s=0.3)
plt.xlabel('TimeStamp')
plt.ylabel('Normalised Magnitude Y')
plt.subplot(2,2,3)
plt.scatter(y,Nz,s=0.3)
plt.xlabel('TimeStamp')
plt.ylabel('Normalised Magnitude Z')
plt.savefig('BarGraph1.png',dpi = 300)
    
    
    
    
    
    









