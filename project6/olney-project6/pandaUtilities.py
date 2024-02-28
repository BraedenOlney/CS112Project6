# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 17:48:24 2022

@author: Braeden Olney
"""

import pandas as pd
import numpy as np

def getFit(xVals, yVals, n):
    """
    Assumes xVals and yVals are numpy arrays
    Find the regression model given the xVals, yVals, and the power (n)
    of the regression model
    return the predicrted values of this model
    """
    
    #get the coefficient of this model
    fit = np.polyfit(xVals, yVals, n)
    #return the numpy array of the values predicted by this model
    return np.polyval(fit, xVals)

def readFile(inFile):
    """
    Assumes inFile is a string which is teh name of the .csv file to be read
    Returns the data frame that is constructed by reading the file
    """
    
    #open the fole to be read
    in_handle = open(inFile, 'r')
    
    #read the file
    df = pd.read_csv(in_handle)
    
    #close the file that was read
    in_handle.close()
    
    #return the data frame that was read
    return df

def writeFile(outFile, df):
    """
    Assumes outFile is a string which is the name of the csv file to be written 
    Assuems df is a data frame that will be written to the file
    """
    
    #open the file to be written 
    out_handle = open(outFile, 'w')
    
    #write the revised DataFrame to file
    df.to_csv(out_handle, sep=',', float_format = '%.4f', index=False, index_label=None, mode='w', line_terminator='\n')
    
    #close the file that was written 
    out_handle.close()
    
def get_index_list(strt, stop, dFrm):
    """
    Assumes strt and stop are pos ints which specifiy thh beginning and 
    the endin of the idex values to return 
    Assumes dfrm is a panda data frame
    return the nupu array of the index values, as ints
    """
    index = dFrm.loc[strt:stop:].index
    return np.array(index, dtype = int)

