# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 12:00:39 2019

@author: jroysu
"""

import glob
import csv
import math
import numpy as np
from scipy.stats import pearsonr as pr
path = "*.csv"
#Train Data
Classifier = {}
for fname in glob.glob(path):
    name = fname.split('.')
    FeatureVector = []
    with open(fname) as csf:
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
        MedianX.sort()
        MedianY.sort()
        MedianZ.sort()
        sumXavg = sumX / counter
        sumYavg = sumY / counter
        sumZavg = sumZ / counter
    counter1 = counter
    counter1 = int((counter1+1)/2) + 1
    Q1 = int((counter1+1)/4) + 1
    Q3 = int((counter1+1)*3/4) + 1

#Kurtosis calculation
    with open(fname) as csf:
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
#Standard Deviation and Variance Calculation
    with open(fname) as csf:
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
    
#Calculating Coefficient of Variation and Inverse of Coefficient of Variation
    CVx = (SDx / sumXavg) * 100
    CVy = (SDy / sumYavg) * 100
    CVz = (SDz / sumZavg) * 100


    ICVx = 1/CVx
    ICVy = 1/CVy
    ICVz = 1/CVz

#Skewness Calculation
    with open(fname) as csf:
        csv_reader = csv.reader(csf,delimiter=',')
        Sxnumerator = 0.0
        Synumerator = 0.0
        Sznumerator = 0.0
        for row in csv_reader:
            Sxnumerator = Sxnumerator + (float(row[0]) - sumXavg)**3
            Sxnumerator = Sxnumerator + (float(row[1]) - sumYavg)**3
            Sxnumerator = Sxnumerator + (float(row[2]) - sumZavg)**3
        Sx = math.sqrt((Sxnumerator / ((counter -1)*(Vx**3)))**2)
        Sy = math.sqrt((Synumerator / ((counter -1)*(Vy**3)))**2)
        Sz = math.sqrt((Sznumerator / ((counter -1)*(Vz**3)))**2)

#Trimmed Mean
    TrMeanX = MedianX[1:counter]
    TrMeanX = np.mean(TrMeanX)
    TrMeanY = MedianY[1:counter]
    TrMeanY = np.mean(TrMeanY)
    TrMeanZ = MedianZ[1:counter]
    TrMeanZ = np.mean(TrMeanZ)

#Pearson's Coefficient for a single sample
    with open(fname) as csf1:
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
        PearsonSamplingCoefficient = math.sqrt((sumNumerator / sumDenominator)*(sumNumerator / sumDenominator))

#Calculating 2,7,12,....97 Percentile values
    P2 = int(0.02*counter) + 1
    P7 = int(0.07*counter) + 1
    P12 = int(0.12*counter) + 1
    P17 = int(0.17*counter) + 1
    P22 = int(0.22*counter) + 1
    P27 = int(0.27*counter) + 1
    P32 = int(0.32*counter) + 1
    P37 = int(0.37*counter) + 1
    P42 = int(0.42*counter) + 1
    P47 = int(0.47*counter) + 1
    P52 = int(0.52*counter) + 1
    P57 = int(0.57*counter) + 1
    P62 = int(0.62*counter) + 1
    P67 = int(0.67*counter) + 1
    P72 = int(0.72*counter) + 1
    P77 = int(0.77*counter) + 1
    P82 = int(0.82*counter) + 1
    P87 = int(0.87*counter) + 1
    P92 = int(0.92*counter) + 1
    P97 = int(0.97*counter) + 1
    
    FeatureVector.append(Kx)
    FeatureVector.append(Ky)
    FeatureVector.append(Kz)
    FeatureVector.append(sumXavg)
    FeatureVector.append(sumYavg)
    FeatureVector.append(sumZavg)
    FeatureVector.append(MedianX[counter1])
    FeatureVector.append(MedianY[counter1])
    FeatureVector.append(MedianZ[counter1])
    FeatureVector.append(MedianX[Q1])
    FeatureVector.append(MedianY[Q1])
    FeatureVector.append(MedianZ[Q1])
    FeatureVector.append(MedianX[Q3])
    FeatureVector.append(MedianY[Q3])
    FeatureVector.append(MedianZ[Q3])
    FeatureVector.append(SDx)
    FeatureVector.append(SDy)
    FeatureVector.append(SDz)
    FeatureVector.append(Vx)
    FeatureVector.append(Vy)
    FeatureVector.append(Vz)
    FeatureVector.append(CVx)
    FeatureVector.append(CVy)
    FeatureVector.append(CVz)
    FeatureVector.append(ICVx)
    FeatureVector.append(ICVy)
    FeatureVector.append(ICVz)
    FeatureVector.append(Sx)
    FeatureVector.append(Sy)
    FeatureVector.append(Sz)
    FeatureVector.append(TrMeanX)
    FeatureVector.append(TrMeanY)
    FeatureVector.append(TrMeanZ)
    #FeatureVector.append(PearsonSamplingCoefficient)
    #FeatureVector.append(P2)
    #FeatureVector.append(P7)
    #FeatureVector.append(P12)
    #FeatureVector.append(P17)
    #FeatureVector.append(P22)
    #FeatureVector.append(P27)
    #FeatureVector.append(P32)
    #FeatureVector.append(P37)
    #FeatureVector.append(P42)
    #FeatureVector.append(P47)
    #FeatureVector.append(P52)
    #FeatureVector.append(P57)
    #FeatureVector.append(P62)
    #FeatureVector.append(P67)
    #FeatureVector.append(P72)
    #FeatureVector.append(P77)
    #FeatureVector.append(P82)
    #FeatureVector.append(P87)
    #FeatureVector.append(P92)
    #FeatureVector.append(P97)
    
#    print(FeatureVector)
    Classifier[name[0]] = FeatureVector
#print(Classifier.keys())
#print(pr(Classifier['392D-iOS'],Classifier['382A-iOS']))
#Test Data
#pearsonCoffecient = 0.0
#Key = ''
#for i in Classifier:
#    pearsonCoffecient1 = pr(Classifier['382A-iOS'],Classifier[i])
#    pearsonCoffecient2 = pearsonCoffecient1[0]
##    print(pearsonCoffecient1[0])
#    if(pearsonCoffecient2 > pearsonCoffecient):
#        pearsonCoffecient = pearsonCoffecient2
#        Key = i
#print('The identified Location is',Key)
print(Classifier)
