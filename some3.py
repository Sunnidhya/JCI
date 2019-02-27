# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 10:15:46 2019

@author: jroysu
"""

import csv
import csv
with open('389atChair-iOS.csv') as csf:
    csv_reader = csv.reader(csf,delimiter = ',')
    
    for row in csv_reader:
        print(float(row[0]))