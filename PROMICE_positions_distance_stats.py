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
stats=np.zeros((7,len(meta)))
date0=['']*len(meta)
date1=['']*len(meta)
years=np.zeros(len(meta))

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


        if ly=='p': plt.savefig('./figs/'+stnam+'.png', dpi=72,bbox_inches = 'tight')
        if ly=='x':plt.show()


df2 = pd.DataFrame(columns=['name','start','end','delta time','lat0','lat1','lon0','lon1','displacement meters','elev0','elev1','delta elev'])
df2["name"]=pd.Series(meta.name)
df2["start"]=pd.Series(date0[:])
df2["end"]=pd.Series(date1[:])
df2["lat0"]=pd.Series(stats[0,:])
df2["lat1"]=pd.Series(stats[1,:])
df2["lon0"]=pd.Series(stats[2,:])
df2["lon1"]=pd.Series(stats[3,:])
df2["elev0"]=pd.Series(stats[4,:])
df2["elev1"]=pd.Series(stats[5,:])
df2["displacement meters"]=pd.Series(stats[6,:])
df2["delta elev"]=df2["elev1"]-df2["elev0"]
df2["delta time"]=pd.Series(years[:])

if wo:df2.to_csv('./stats/PROMICE_positions_distance_stats.csv')