# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 09:27:50 2019

@author: jroysu
"""

import csv
from matplotlib import pyplot as plt

with open('MagnetometerPixel.csv') as csf:
    csv_reader = csv.reader(csf,delimiter = ',')
    y = []
    z = []
    counter = 0
    for row in csv_reader:
        counter = counter + 1
        y.append(counter)
        z.append(row[1])
        print(row[0] + "          " + row[1]+ "           " +row[2])
    
    plt.scatter(y,z,s=5)
    plt.xlabel('Time')
    plt.ylabel('Pitch')
    plt.savefig('pitch.png',dpi = 300)
    plt.show()