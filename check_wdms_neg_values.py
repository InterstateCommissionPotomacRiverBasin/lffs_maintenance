# -*- coding: utf-8 -*-
"""
01/19/2018

Description: extract and plot met and orad wdms if there are negative values
in them

Input(s): .wdm 
Output(s): .txt and .png files

@author: aseck@icprb.org
Things To improve: create figures folders if
 they do not exist and use arrays 
 for the met and prad variables
"""
#------------Import Python Modules-----------#
import os
from wdmtoolbox import wdmtoolbox
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.image as mpimg
import glob
import datetime
#--------------------------------------------#
#---------------------------------------------------------------------------#
#---Define input/output file directories------------------------------------#

metdirectory= "Z:\MODEL\p52fc04_sa\input\scenario\climate\met\met8416e"
path1= "Z:\MODEL\p52fc04_sa\output\icprb\wdmcheck\met8416e"
praddirectory= "Z:\MODEL\p52fc04_sa\input\scenario\climate\prad\prad8416e"
path3= "Z:\MODEL\p52fc04_sa\output\icprb\wdmcheck\prad8416e"

#---------------------------------------------------------------------------#
#---Define input/output file directories------------------------------------#
   
myFmt = mdates.DateFormatter('%m/%d')

#---------------------------------------------------------------------------#
#---get the date correcponding to three months ago--------------------------#

import datetime
i = datetime.datetime.now()
currentdate = i
#print i.month-1
if(i.month-3<=0): 
    correctmonth=i.month+9
else: 
    correctmonth=i.month-3
if(i.month-3<=0): 
    correctyear=i.year-1
else: 
    correctyear=i.year
todaysdate=datetime.datetime(i.year,i.month,i.day)
#print todaysdate
threemonthago=datetime.datetime(correctyear,correctmonth,i.day)
#print threemonthago

#---------------------------------------------------------------------------#
#---going through the met files and prnt files with issues------------------#
allFiles = glob.glob(metdirectory + "/*met*.wdm*")
print 'Check the following files for negative values in wdms'


for file_ in allFiles:
    title = file_[-10:-4]
    figurename = path1+ "/atmp/atmp_" +  title + ".png"
    dataatmp=wdmtoolbox.extract(file_,1004)
    df=dataatmp
    nv=df[(df < 0).all(1)]
    textfile =  path1+ "/atmp/atmp_" +  title + ".txt" 
    if not nv.empty:
        print figurename
        #f1=open(textfile)
        f1=textfile
        nv.to_csv(f1)
        #f1.close()
        fig, ax = plt.subplots()
        ax.plot(dataatmp)
        ax.set_xlim([threemonthago, currentdate])
        ax.xaxis.set_major_formatter(myFmt)
        ax.set_ylim([-20, 110])
        plt.ylabel('Temperature (F)')
        plt.title(title)
        plt.savefig(figurename)
    
    figurename2 = path1+ "/wndh/wndh_" +  title + ".png"
    datawndh=wdmtoolbox.extract(file_,1002)
    df=datawndh
    nv=df[(df < 0).all(1)]
    textfile =  path1+ "/wndh/wndh_" +  title + ".txt" 
    if not nv.empty:
        print figurename2
         #f1=open(textfile)
        f1=textfile
        nv.to_csv(f1)
        #f1.close()
        fig, ax = plt.subplots()
        ax.plot(datawndh)
        ax.set_xlim([threemonthago, currentdate])
        ax.xaxis.set_major_formatter(myFmt)
        ax.set_ylim([-20, 110])
        plt.ylabel('Wind ()')
        plt.title(title)
        plt.savefig(figurename2)
      
    #evapotranspiration
    figurename3 = path1+ "/evap/evap_" +  title + ".png"
    dataevap=wdmtoolbox.extract(file_,1000)
    df=dataevap
    nv=df[(df < 0).all(1)]
    textfile =  path1+ "/evap/evap_" +  title + ".txt" 
    if not nv.empty:
        print figurename3
        #f1=open(textfile)
        f1=textfile
        nv.to_csv(f1)
        #f1.close()
        fig, ax = plt.subplots()
        ax.plot(dataevap)
        ax.set_xlim([threemonthago, currentdate])
        ax.xaxis.set_major_formatter(myFmt)
        ax.set_ylim([-0.05,0.05])
        plt.ylabel('Evapotranspiration ()')
        plt.title(title)
        plt.savefig(figurename3)
    #"""
    #"""
    #dewpointtemp
    figurename4 = path1+ "/dewp/dewp_" +  title + ".png"
    datadewp=wdmtoolbox.extract(file_,1001)
    df=datadewp
    nv=df[(df < 0).all(1)]
    textfile =  path1+ "/dewp/dewp_" +  title + ".txt" 
    if not nv.empty:
        print figurename4
         #f1=open(textfile)
        f1=textfile
        nv.to_csv(f1)
        #f1.close()
        fig, ax = plt.subplots()
        ax.plot(datadewp)
        ax.set_xlim([threemonthago, currentdate])
        ax.xaxis.set_major_formatter(myFmt)
        ax.set_ylim([-20,100])
        plt.ylabel('Dew point temperature (F)')
        plt.title(title)
        plt.savefig(figurename4)
        #"""
   
    #radh
    figurename5 = path1+ "/radh/radh_" +  title + ".png"
    dataradh=wdmtoolbox.extract(file_,1003)
    df=dataradh
    nv=df[(df < 0).all(1)]
    textfile =  path1+ "/radh/radh_" +  title + ".txt" 
    if not nv.empty:
        print figurename5
         #f1=open(textfile)
        f1=textfile
        nv.to_csv(f1)
        #f1.close()
        fig, ax = plt.subplots()
        ax.plot(dataradh)
        ax.set_xlim([threemonthago, currentdate])
        ax.xaxis.set_major_formatter(myFmt)
        ax.set_ylim([-20,100])
        plt.ylabel('Solar Radiation()')
        plt.title(title)
        plt.savefig(figurename5)
    
   
   

   
allFiles2 = glob.glob(praddirectory + "/*prad*.wdm*")
for file_ in allFiles2:
    figurename6 = path3+ "/hprc/hprc_" +  title + ".png"
    title = file_[-10:-4]
      
    datahprc=wdmtoolbox.extract(file_,2000)
    df=datahprc
    nv=df[(df < 0).all(1)]
    textfile =  path1+ "/hprc/hprc_" +  title + ".txt" 
    if not nv.empty:
        print figurename6
         #f1=open(textfile)
        f1=textfile
        nv.to_csv(f1)
        #f1.close()
        fig, ax = plt.subplots()
        ax.plot(datahprc)
        ax.set_xlim([threemonthago, currentdate])
        ax.xaxis.set_major_formatter(myFmt)
        ax.set_ylim([-0.05,2])
        plt.ylabel('Precipitation()')
        plt.title(title)
        plt.savefig(figurename6)
    

    
print "Finished making met and prad figures in " +path1 + " and " + path3 + ". Please take a look"