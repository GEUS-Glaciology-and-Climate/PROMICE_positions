#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@authors:
    Adrien Wehrlé, University of Zurich, Switzerland
    Jason Box, GEUS

"""

import time
import os
import numpy as np
from pyproj import Transformer
from typing import Tuple
from scipy import interpolate
import matplotlib.pyplot as plt
import pandas as pd


# -------------------------------- chdir
if os.getlogin() == 'jason':
    base_path = '/Users/jason/Dropbox/AWS/GCNET/GCNet_positions'

os.chdir(base_path)

def output_kml(site,datex,lat,lon):
    kml = simplekml.Kml(open=1)
    
    pnt = kml.newpoint(name=site+' '+datex)
    pnt.coords=[(lon,lat)]
    pnt.style.labelstyle.color = simplekml.Color.red  # Make the text red
    pnt.style.labelstyle.scale = 1.5  # text scaling multiplier
    pnt.style.iconstyle.icon.href = 'http://maps.google.com/mapfiles/kml/shapes/placemark_circle.png'
    pnt.altitudemode = simplekml.AltitudeMode.relativetoground
    
    kml_ofile='./output/kml/'+site+'_'+datex+".kml"
    kml.save(kml_ofile)

def reproject_points(
    xcoords: list,
    ycoords: list,
    in_projection: str = "4326",
    out_projection: str = "3413",
) -> Tuple[list, list]:

    inProj = f"epsg:{in_projection}"
    outProj = f"epsg:{out_projection}"

    trf = Transformer.from_crs(inProj, outProj, always_xy=True)
    x_coords, y_coords = trf.transform(xcoords, ycoords)

    return x_coords, y_coords

## %% site coordinates

lon_t0 = -49.295583 # 1990
lat_t0 =  69.573694 # 1990

lon_t1 = -49.3707 # 2021-08-31
lat_t1 = 69.5538 # 2021-08-31

print('lat_t0, lon_t0',lat_t0, lon_t0)
print('lat_t1, lon_t1',lat_t1, lon_t1)

SC_3413x_1990, SC_3413y_1990 = reproject_points(lon_t0, lat_t0)
SC_3413x_2021, SC_3413y_2021 = reproject_points(lon_t1, lat_t1)

## %% site trajectory

trajectory_x = [SC_3413x_1990, SC_3413x_2021]
trajectory_y = [SC_3413y_1990, SC_3413y_2021]

times = [1990, 2022]
x_ft = interpolate.interp1d(times, trajectory_x, kind="linear",fill_value="extrapolate")
y_ft = interpolate.interp1d(times, trajectory_y, kind="linear",fill_value="extrapolate")


target_date='2021-11-15'
target_date='2000-06-15'
target_date='2030-06-15'
t = pd.to_datetime(target_date)

decimal_year = (float(t.strftime("%j")) - 1) / 366 + float(t.strftime("%Y"))

print('target_date',target_date,'decimal_year',decimal_year)

SC_xt = x_ft(decimal_year)
SC_yt = y_ft(decimal_year)

trf = Transformer.from_crs("epsg:3413", "epsg:4326", always_xy=True)
lon_tx,lat_tx  = trf.transform(SC_xt, SC_yt)

print('lat_tx, lon_tx',lat_tx, lon_tx)

import simplekml

site='SWC'

output_kml(site,'1990',lat_t0,lon_t0)
output_kml(site,'2021-08-31',lat_t1,lon_t1)
output_kml(site,target_date,lat_tx,lon_tx)


