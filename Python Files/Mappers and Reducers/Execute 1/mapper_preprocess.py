#!/usr/bin/env python
# coding: utf-8

# In[1]:


# mapper_preprocess.py
import sys
import csv

for line in sys.stdin:
    data = list(csv.reader([line]))[0]
    try:
        if data[-2] == '':  # change_percent
            data[-2] = '0.0'  # Replace with 0
        if data[-1] == '':  # avg_vol_20d
            data[-1] = '0.0'  # Replace with 0
        print(",".join(data))
    except:
        continue

