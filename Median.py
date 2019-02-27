# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 14:16:59 2019

@author: jroysu
"""

import csv
with open('prasanna to last cub alvina 5.csv') as csf:
    csv_reader = csv.reader(csf,delimiter = ',')
    x = []
    y = []
    z = []
    counter = 0
    for row in csv_reader:
        x.append(float(row[0]))
        y.append(float(row[1]))
        z.append(float(row[2]))
        counter = counter + 1
    x.sort()
    y.sort()
    z.sort()
counter = (counter + 1)/2
count = int(counter + 1)
print('Median values are Mx: {} My: {} Mz: {}'.format(x[count],y[count],z[count]))
