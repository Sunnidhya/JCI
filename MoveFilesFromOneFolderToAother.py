# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 10:45:01 2019

@author: jroysu
"""

import shutil
import os
source = 'C:/Users/jroysu/Desktop/DEB GET/Mobility/Data25thFebruary/'
destination = "C:/Users/jroysu/Desktop/DEB GET/Mobility/TrainData/Today'sData/"

files = os.listdir(source)

for f in files:
    shutil.move(source+f,destination)