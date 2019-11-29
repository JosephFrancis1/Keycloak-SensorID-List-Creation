#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import sys

file = sys.argv[1]

sensors = pd.read_csv(file)

sensors["combined"] = sensors.deviceuid + '##'

sensors.head()

l = [''.join(sensors['combined'])]
l = (", ".join(str(f) for f in l))        #removes brackets
l = l[:-2]				  #removes final 2 characters

print(l)
