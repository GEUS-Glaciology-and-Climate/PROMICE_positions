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
ly='p' # p for .png, x for console only
wo=1

meta=pd.read_csv('./meta/site_info.csv')
# print(meta.columns)

# site by site position stats
stats=np.zeros((6,len(meta)))

for st,stnam in enumerate(meta.name):

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
            ax[cc].plot(df['date'],df['LatitudeGPS_HDOP<1(degN)'],'.')
            ax[0].set_title(stnam+' latitude')

            cc+=1
            ax[cc].plot(df['date'],lon,'.')
            ax[cc].set_title(stnam+' longitude')
    
            cc+=1
            ax[cc].plot(df['date'],elev,'.')
            ax[cc].set_title(stnam+' elevation')
            ax[cc].set_ylabel('meters a.s.l')
        
        v=np.where(~np.isnan(df['lat']))
        v=v[0]
        n=len(v)
        print(v[0],df['date'][v[0]])

        cc=0        
        stats[0,st]=lat[v[0]] 
        ax[cc].plot(df['date'][v[0]],stats[0,st],'s',color='r')        
        stats[1,st]=lat[v[n-1]]
        ax[cc].plot(df['date'][v[n-1]],stats[1,st],'s',color='r')

        cc+=1

        stats[2,st]=lon[v[0]] 
        ax[cc].plot(df['date'][v[0]],stats[2,st],'s',color='r')        
        stats[3,st]=lon[v[n-1]]
        ax[cc].plot(df['date'][v[n-1]],stats[3,st],'s',color='r')

        cc+=1

        stats[4,st]=elev[v[0]] 
        ax[cc].plot(df['date'][v[0]],stats[4,st],'s',color='r')        
        stats[5,st]=elev[v[n-1]]
        ax[cc].plot(df['date'][v[n-1]],stats[5,st],'s',color='r')
        
        if ly=='p': plt.savefig('./figs/'+stnam+'.png', dpi=100,bbox_inches = 'tight',pad_inches = 0)
        if ly=='x':plt.show()


df2 = pd.DataFrame(columns=['name','lat0','lat1','lon0','lon1','elev0','elev1','delta elev'])
df2["name"]=pd.Series(meta.name)
df2["lat0"]=pd.Series(stats[0,:])
df2["lat1"]=pd.Series(stats[1,:])
df2["lon0"]=pd.Series(stats[2,:])
df2["lon1"]=pd.Series(stats[3,:])
df2["elev0"]=pd.Series(stats[4,:])
df2["elev1"]=pd.Series(stats[5,:])
df2["delta elev"]=df2["elev1"]-df2["elev0"]

if wo:df2.to_csv('./stats/PROMICE_position_stats.csv')