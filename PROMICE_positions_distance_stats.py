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
import geopy.distance

th=1 ; th=2 # thickness
formatx='{x:,.3f}'; fs=24 ; fs=16 # font size
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


working_dir='/Users/jason/Dropbox/AWS/PROMICE/PROMICE_Positions/' # change this in your local system
os.chdir(working_dir)

# graphics layout option
ly='p' # p for .png, x for console only
wo=1 # write out stats
write_fig=0 # write out figures

# read site meta data
meta=pd.read_csv('./meta/site_info.csv')
# print(meta.columns)

# site by site position stats
stats=np.zeros((7,len(meta)))
date0=['']*len(meta)
date1=['']*len(meta)
years=np.zeros(len(meta))

# loop over sites
for st,stnam in enumerate(meta.name):
# for st,stnam in enumerate(meta.name[0:2]):

    stnam=stnam.lstrip()
    fn='/Users/jeb/Google Drive/PROMICE/AWS_updates/'+stnam+'_month_v03_upd.txt'
    # if stnam=='QAS_L':
    # if stnam=='KAN_M':
    if stnam!='KAN_B':
    # if st==25:
        plt.close()
        fig, ax = plt.subplots(3,1,figsize=(10,15))
        
        cc=0

        print(st,fn)
        df=pd.read_csv(fn, delim_whitespace=True)
        df['day']=15
        df['month']=df['MonthOfYear']
        df['year']=df['Year']
        df['date']=pd.to_datetime(df[["year", "month","day"]])

        lat=df['LatitudeGPS_HDOP<1(degN)'] ; lat[lat<0]=np.nan
        df['lat']=df['LatitudeGPS_HDOP<1(degN)'] ; df['lat'][df['lat']<0]=np.nan
        lon=df['LongitudeGPS_HDOP<1(degW)'] ; lon[lon<0]=np.nan
        elev=df['ElevationGPS_HDOP<1(m)'] ; elev[elev<0]=np.nan

        if stnam=='KPC_L':
            df['lat'][df['date']>'2020-06-15']=np.nan
            df['lat'][df['date']<'2008-11-15']=np.nan
        if stnam=='KPC_U':
            df['lat'][df['date']>'2020-06-15']=np.nan
        if stnam=='TAS_L':
            df['lat'][df['date']>'2020-07-15']=np.nan
            df['lat'][df['date']<'2008-11-15']=np.nan
        if stnam=='TAS_U':
            # df['lat'][df['date']>'2020-07-15']=np.nan
            df['lat'][df['date']<'2008-11-15']=np.nan
        if stnam=='QAS_U':
            df['lat'][df['date']>'2020-06-15']=np.nan
            # df['lat'][df['date']<'2009-09-15']=np.nan
        if stnam=='QAS_L':
            df['lat'][df['date']>'2020-06-15']=np.nan
            df['lat'][df['date']<'2009-09-15']=np.nan
        if stnam=='NUK_L':
            df['lat'][df['date']>'2020-07-15']=np.nan
            df['lat'][df['date']<'2007-11-15']=np.nan
        if stnam=='NUK_U':
            df['lat'][df['date']>'2020-08-15']=np.nan
            df['lat'][df['date']<'2008-11-15']=np.nan
        if stnam=='NUK_K':
            df['lat'][df['date']>'2020-07-15']=np.nan
            # df['lat'][df['date']<'2008-11-15']=np.nan
        if stnam=='UPE_L':
            df['lat'][df['date']>'2020-07-15']=np.nan
            # df['lat'][df['date']<'2008-11-15']=np.nan
        if stnam=='UPE_U':
            df['lat'][df['date']>'2020-07-15']=np.nan
            # df['lat'][df['date']<'2008-11-15']=np.nan
        if stnam=='THU_L':
            df['lat'][df['date']>'2020-06-15']=np.nan
            # df['lat'][df['date']<'2008-11-15']=np.nan
        if stnam=='THU_U':
            df['lat'][df['date']>'2020-06-15']=np.nan
            # df['lat'][df['date']<'2008-11-15']=np.nan
        if stnam=='EGP':
            df['lat'][df['date']>'2020-06-15']=np.nan
            # df['lat'][df['date']<'2008-11-15']=np.nan

        # print(df.columns)
        

        if ly!='n':
            ax[cc].plot(df['date'],df['LatitudeGPS_HDOP<1(degN)'],'.',color='k')
            ax[0].set_title(stnam+' latitude')

            cc+=1
            ax[cc].plot(df['date'],lon,'.',color='k')
            ax[cc].set_title(stnam+' longitude')
    
            cc+=1
            ax[cc].plot(df['date'],elev,'.',color='k')
            ax[cc].set_ylabel('meters a.s.l')
        
        v=np.where(~np.isnan(df['lat']))
        v=v[0]
        n=len(v)
        print(v[0],df['date'][v[0]])
        x=[df['date'][v[0]],df['date'][v[n-1]]]




        cc=0        
        stats[0,st]=lat[v[0]] 
        ax[cc].plot(df['date'][v[0]],stats[0,st],'s',color='g',alpha=0.5,label='first valid datum')        
        stats[1,st]=lat[v[n-1]]
        ax[cc].plot(df['date'][v[n-1]],stats[1,st],'s',color='r',alpha=0.5,label='last valid datum')
        y=[stats[0,st],stats[1,st]]
        ax[cc].plot(x, y, '--',c='b',label='approximation')
        ax[cc].legend()

        cc+=1

        stats[2,st]=lon[v[0]] 
        ax[cc].plot(df['date'][v[0]],stats[2,st],'s',color='g',alpha=0.5)        
        stats[3,st]=lon[v[n-1]]
        ax[cc].plot(df['date'][v[n-1]],stats[3,st],'s',color='r',alpha=0.5)

        y=[stats[2,st],stats[3,st]]
        ax[cc].plot(x, y, '--',c='b')

        cc+=1

        stats[4,st]=elev[v[0]] 
        ax[cc].plot(df['date'][v[0]],stats[4,st],'s',color='g',alpha=0.5)        
        stats[5,st]=elev[v[n-1]]
        ax[cc].plot(df['date'][v[n-1]],stats[5,st],'s',color='r',alpha=0.5)
        
        de=stats[5,st]-stats[4,st]

        ax[2].set_title(stnam+' elevation, change = '+str('%.0f'%de)+' m')

        y=[stats[4,st],stats[5,st]]
        ax[cc].plot(x, y, '--',c='b')
        
        coords_1 = (stats[0,st],stats[2,st])
        coords_2 = (stats[1,st],stats[3,st])
        stats[6,st]=geopy.distance.distance(coords_1, coords_2).m
        # print(df.name[k],df.name[k],str("%.0f"%(dist)))
        
        date0[st]=df['date'][v[0]]
        date1[st]=df['date'][v[n-1]]
        
        duration = df['date'][v[n-1]] - df['date'][v[0]]                         # For build-in functions
        duration_in_s = duration.total_seconds()
        years[st] = divmod(duration_in_s, 86400)[0]/365.25
        print(years[st])


        if ((ly=='p')&(write_fig)): plt.savefig('./figs/'+stnam+'.png', dpi=72,bbox_inches = 'tight')
        if ly=='x':plt.show()


df2 = pd.DataFrame(columns=['site name','first valid date','latest valid date','delta time','first valid latitude, °N','latest valid latitude, °N','first valid longitude, °W','latest valid longitude, °W','displacement, m','displacement rate, m/y','first valid elevation, m','latest valid elevation, m','elevation change, m'])
df2['site name']=pd.Series(meta.name)
df2['first valid date']=pd.Series(date0[:])
df2['latest valid date']=pd.Series(date1[:])
df2['first valid latitude, °N']=pd.Series(stats[0,:])
df2['latest valid latitude, °N']=pd.Series(stats[1,:])
df2['first valid longitude, °W']=pd.Series(stats[2,:])
df2['latest valid longitude, °W']=pd.Series(stats[3,:])
df2['first valid elevation, m']=pd.Series(stats[4,:])
df2['latest valid elevation, m']=pd.Series(stats[5,:])
df2["displacement, m"]=pd.Series(stats[6,:])
df2['elevation change, m']=df2['latest valid elevation, m']-df2['first valid elevation, m']
df2["delta time"]=pd.Series(years[:])

df2["displacement rate, m/y"]=df2["displacement, m"]/df2["delta time"]
df2["displacement rate, m/y"][df2['site name']=='KAN_B']=np.nan
df2['displacement, m'] = df2['displacement, m'].map(lambda x: '%.0f' % x)
df2['elevation change, m'] = df2['elevation change, m'].map(lambda x: '%.0f' % x)
df2['delta time'] = df2['delta time'].map(lambda x: '%.1f' % x)
df2['first valid elevation, m'] = df2['first valid elevation, m'].map(lambda x: '%.0f' % x)
df2['latest valid elevation, m'] = df2['latest valid elevation, m'].map(lambda x: '%.0f' % x)
df2['first valid latitude, °N'] = df2['first valid latitude, °N'].map(lambda x: '%.4f' % x)
df2['latest valid latitude, °N'] = df2['latest valid latitude, °N'].map(lambda x: '%.4f' % x)
df2['first valid longitude, °W'] = df2['first valid longitude, °W'].map(lambda x: '%.4f' % x)
df2['latest valid longitude, °W'] = df2['latest valid longitude, °W'].map(lambda x: '%.4f' % x)
df2['displacement rate, m/y'] = df2['displacement rate, m/y'].map(lambda x: '%.1f' % x)

if wo:df2.to_csv('./stats/PROMICE_positions_distance_stats.csv',sep=';')
if wo:df2.to_excel('./stats/PROMICE_positions_distance_stats.xlsx')

print("average displacement rate",np.nanmean(df2["displacement rate, m/y"].astype(float)))
print("average displacement rate",np.nanstd(df2["displacement rate, m/y"].astype(float)))
print("elevation change, m",np.nanmean(df2["elevation change, m"].astype(float)))
print("elevation change, m",np.nanstd(df2["elevation change, m"].astype(float)))
