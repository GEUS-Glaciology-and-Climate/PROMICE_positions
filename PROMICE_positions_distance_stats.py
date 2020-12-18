#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 11:17:20 2020

@author: jason box, jeb@geus.dk

compute statistics on PROMICE station positions

"""

import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import datetime
# from datetime import datetime
# from matplotlib.pyplot import figure
import geopy.distance

th=1 ; th=2
formatx='{x:,.3f}'; fs=24 ; fs=16
plt.rcParams["font.size"] = fs
plt.rcParams['axes.facecolor'] = 'w'
plt.rcParams['axes.edgecolor'] = 'k'
plt.rcParams['axes.grid'] = False
# plt.rcParams['axes.grid'] = True
plt.rcParams['grid.alpha'] = 0.8
plt.rcParams['grid.color'] = "#cccccc"
plt.rcParams["legend.facecolor"] ='w'
plt.rcParams["mathtext.default"]='regular'
plt.rcParams['grid.linewidth'] = th/2
plt.rcParams['axes.linewidth'] = 1
mult_legend=0.8
axis_mult=1

path0='/Users/jason/Dropbox/AW/'

os.chdir('/Users/jason/Dropbox/AWS/PROMICE/PROMICE_Positions/')

# graphics layout option
ly='x' # p for .png, x for console only
wo=1

fn='./stats/PROMICE_position_stats.csv'
df=pd.read_csv(fn)

print(df.columns)

df[]
for k in range(0,len(df)):

    df.name[k]
    # print(k,df.name[k])
    coords_1 = (df.lat0[k],df.lon0[k])
    coords_2 = (df.lat1[k],df.lon1[k])
    dist=geopy.distance.distance(coords_1, coords_2).m
    print(df.name[k],df.name[k],str("%.0f"%(dist)))
    # out.iloc[k,j]=nm[k,j]
