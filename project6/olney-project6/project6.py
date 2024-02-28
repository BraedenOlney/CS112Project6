# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 14:48:22 2022

@author: Braeden Olney
"""
import utilitiesModule as um
import pandaUtilities as pdu
import matplotlib.pyplot as plt

def plotData(pDegrees, start, stop, dFrm):
    """Assuems:
    pDegrees is a list of ints of regression model degrees
    strart is an int which is the beginning of te subset to plot
    stop is an int which is the end of the subset to plot
    dFrm is the DataFrame
    strCol is a string which specifies the column to plot on y axis
    Fuction plots the experimental data and the models specified by pDegrees
    The index values are  on the x axis
    the data are predicted valeus int eh column specifired bu strCol are the y axix
    """
    #format string that will be plot title
    strTitle = 'AudUsd Ave Month Prices: months ', start, ' to ', stop
    
    #set iup the figure
    plt.figure()
    
    if(start != 0 or stop != 248):
        #construct numpy array of the colums data
        nStop = 248-stop
        nStart = start-1
        yVals =  dFrm['Average'][:-nStop][nStart:].to_numpy()
        #set up numpy array of vals on y axis
        xVals = dFrm['Date'][:-nStop][nStart:].to_numpy()
        #temp = start
        #while(temp > 0):
         #   yVals.delete[0]
          #  yVals.delete[0]
           # temp = temp -1
           
    else:
        #construct numpy array of the colums data
        yVals =  dFrm['Average'].to_numpy()
        #set up numpy array of vals on y axis
        xVals = dFrm['Date'].to_numpy()
    
    #get the indexVals of rthe data frame rows
    indexVals = pdu.get_index_list(start, stop, dFrm)
    
    #first plot the experimental data
    plt.plot(xVals, yVals, 'black', label = strTitle)
    #iterate through all values of n in pDegrees
    for n in pDegrees:
        #get the preducted values of this model
        predict = pdu.getFit(indexVals, yVals, n)
        #set up the strign for the plot
        strFormat = um.formatRegressionGraph(n)
        #now plot the regression model
        strLabel = 'model degree: ' + str(n)
        plt.plot(xVals, predict, strFormat, label = strLabel)
    #after ecititng hte loop annotate the plot
    plt.title(strTitle)
    plt.xlabel('Month')
    plt.ylabel('Price')
    plt.legend(loc = 'best')
    
    
    
###############################################################
inFileName = 'AudUsd.csv'
outFileName = 'AudUsdEdited.csv'

data1 = pdu.readFile(inFileName)

high = data1['High'].to_numpy()
low = data1['Low'].to_numpy()
average = (high +low)/2
date = data1['Date'].to_numpy()

data1['Average'] = average

pdu.writeFile(outFileName, data1)

data2 = pdu.readFile(outFileName)

print('\nthe modified data frame:\n')
print(data2)



#pdu.writeFile(outFileName, usdData)
pDegree = [1,3]  
plotData(pDegree, 0, 248, data2)

plotData(pDegree, 20, 80, data2)
##############################################################



