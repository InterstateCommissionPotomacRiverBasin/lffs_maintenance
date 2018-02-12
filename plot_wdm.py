# -*- coding: utf-8 -*-
"""
01/19/2018

Description: extract and plot met and prad wdms for last 50 days.

Input(s): .wdm 
Output(s): .txt and .png files

@author: aseck@icprb.org

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

maindirectory="Z:\MODEL\p52fc05_sa"
metdirectory= maindirectory + "\input\scenario\climate\met\met8418"
path1= maindirectory + "\output\icprb\wdm_daily_check"
praddirectory= maindirectory + "\input\scenario\climate\prad\prad8418"
psdirectory= maindirectory + '/input/scenario/river/ps/ps0118h1'
divdirectory= maindirectory + '/input/scenario/river/div/div0118h1'
#---------------------------------------------------------------------------#
#---Define input/output file directories------------------------------------#
   
myFmt = mdates.DateFormatter('%d-%b')

#---------------------------------------------------------------------------#
#---get the date correcponding to three months ago--------------------------#

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
#---going through the prad files and make figures for the past 50 days------------------#

ps_wdm = ['ps_B24001_to_PU4_4440_3970.wdm', 'ps_A24031_to_PM1_4250_4500.wdm'] 
dnslist=[3050]
pslist=['ps']
yaxisminlist=[0]
yaxismaxlist=[10]
ylabellist=['Point Source (in)']
            
timelimitlist=[-1200]

#print dsnlist[0]
#print metlist[]
for i in range (0, 1):
    print i
    print dnslist[i]
    print pslist[i]
    print psdirectory
    
    for ps in range(0,len(ps_wdm)):
        file_ = os.path.join(psdirectory,ps_wdm[ps])
        print file_
        title = file_[-30:-4]
        print title
        
        path2=path1+ "/" + pslist[i] +"/"
        if not os.path.exists(path2):
            os.makedirs(path2)
        figurename = path2+ "/" + pslist[i] + "_" +  title + ".png"
        dataatmp=wdmtoolbox.extract(file_,dnslist[i])
        df=dataatmp.ix[timelimitlist[i]:]
        textfile =  path2+ "/" + pslist[i] + "_" +  title + ".txt" 
        #print figurename
        f1=textfile
        df.to_csv(f1)
        fig, ax = plt.subplots()
        ax.plot(df)
        #ax.set_xlim([threemonthago, currentdate])
        ax.xaxis.set_major_formatter(myFmt)
        #ax.set_ylim([yaxisminlist[i], yaxismaxlist[i]])
        plt.ylabel(ylabellist[i])
        plt.title(title)
        fig.tight_layout()
        fig.subplots_adjust(top=0.88)
         
        plt.savefig(figurename)
        plt.close(fig) 
       
 


div_wdm = ['DIV_PM7_4620_4580.wdm', 'DIV_PM7_4580_4820.wdm', 'DIV_PM7_4820_0001.wdm'] 
dnslist=[3057]
divlist=['div']
yaxisminlist=[0]
yaxismaxlist=[10]
ylabellist=['Diversions (in)']
            
timelimitlist=[-1200]

#print dsnlist[0]
#print metlist[]
for i in range (0, 1):
    print i
    print dnslist[i]
    print divlist[i]
    print divdirectory
    
    for div in range(0,len(div_wdm)):
        file_ = os.path.join(divdirectory,div_wdm[div])
        print file_
        title = file_[-21:-4]
        print title
        
        path2=path1+ "/" + divlist[i] +"/"
        if not os.path.exists(path2):
            os.makedirs(path2)
        figurename = path2+ "/" + divlist[i] + "_" +  title + ".png"
        dataatmp=wdmtoolbox.extract(file_,dnslist[i])
        df=dataatmp.ix[timelimitlist[i]:]
        textfile =  path2+ "/" + divlist[i] + "_" +  title + ".txt" 
        #print figurename
        f1=textfile
        df.to_csv(f1)
        fig, ax = plt.subplots()
        ax.plot(df)
        #ax.set_xlim([threemonthago, currentdate])
        ax.xaxis.set_major_formatter(myFmt)
        #ax.set_ylim([yaxisminlist[i], yaxismaxlist[i]])
        plt.ylabel(ylabellist[i])
        plt.title(title)
        fig.tight_layout()
        fig.subplots_adjust(top=0.88)
         
        plt.savefig(figurename)
        plt.close(fig) 





#---------------------------------------------------------------------------#
#---going through the prad files and make figures for the past 50 days------------------#

allFiles = glob.glob(praddirectory + "/*prad*.wdm*")
print 'Check the following files for negative values in wdms'

dnslist=[2000]
pradlist=['hprc']
yaxisminlist=[-1]
yaxismaxlist=[1]
ylabellist=['Precipitation (in)']
            
timelimitlist=[-1200]

#print dsnlist[0]
#print metlist[]
for i in range (0, 1):
    print i
    print dnslist[i]
    print pradlist[i]
    
    for file_ in allFiles:
        title = file_[-10:-4]
        path2=path1+ "/" + pradlist[i] +"/"
        if not os.path.exists(path2):
            os.makedirs(path2)
        figurename = path2+ "/" + pradlist[i] + "_" +  title + ".png"
        dataatmp=wdmtoolbox.extract(file_,dnslist[i])
        df=dataatmp.ix[timelimitlist[i]:]
        textfile =  path2+ "/" + pradlist[i] + "_" +  title + ".txt" 
        #print figurename
        f1=textfile
        df.to_csv(f1)
        fig, ax = plt.subplots()
        ax.plot(df)
        #ax.set_xlim([threemonthago, currentdate])
        ax.xaxis.set_major_formatter(myFmt)
        ax.set_ylim([yaxisminlist[i], yaxismaxlist[i]])
        plt.ylabel(ylabellist[i])
        plt.title(title)
        fig.tight_layout()
        fig.subplots_adjust(top=0.88)
         
        plt.savefig(figurename)
        plt.close(fig)     
    


#---going through the metfiles and make figures for the past 50 days------------------#

allFiles = glob.glob(metdirectory + "/*met*.wdm*")
print 'Check the following files for negative values in wdms'

dnslist=[1004,1000,1002,1001,1003]
metlist=['atmp','evap', 'wndh', 'dewp', 'radh']
yaxisminlist=[-20,-0.05,-20,-20,-20]
yaxismaxlist=[120,0.05,100,120,120]
ylabellist=['Temperature (F)', 'Evaporation (in)', 
            'Wind speed (m/s)', 'Dew Point Temperature (F)', 
            'Solar Radiation (w/m2)']
            
timelimitlist=[-1200,-1200,-1200,-50,-1200]

#print dsnlist[0]
#print metlist[]
for i in range (0, 5):
    print i
    print dnslist[i]
    print metlist[i]
    
    for file_ in allFiles:
        title = file_[-10:-4]
        path2=path1+ "/" + metlist[i] +"/"
        if not os.path.exists(path2):
            os.makedirs(path2)
        figurename = path2+ "/" + metlist[i] + "_" +  title + ".png"
        dataatmp=wdmtoolbox.extract(file_,dnslist[i])
        df=dataatmp.ix[timelimitlist[i]:]
        textfile =  path2+ "/" + metlist[i] + "_" +  title + ".txt" 
        #print figurename
        f1=textfile
        df.to_csv(f1)
        fig, ax = plt.subplots()
        ax.plot(df)
        #ax.set_xlim([threemonthago, currentdate])
        ax.xaxis.set_major_formatter(myFmt)
        ax.set_ylim([yaxisminlist[i], yaxismaxlist[i]])
        plt.ylabel(ylabellist[i])
        plt.title(title)
        fig.tight_layout()
        fig.subplots_adjust(top=0.88)
         
        plt.savefig(figurename)
        plt.close(fig)
     


  

print "Finished making div, ps, met and prad figures in " +path1 + ". Please take a look"