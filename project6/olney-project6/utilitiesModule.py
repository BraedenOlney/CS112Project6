# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 12:59:11 2022

@author: Braeden Olney
"""

import numpy as np
import time
import math

def isValidInteger(strInt):
    """
    Assumes strInt is a string of len >= 1
    Returns True if all chars of the string are numeric:
        else returns False
    """
    #set up named constants for min and max numeric chars
    MIN_UNICODE = ord('0')
    MAX_UNICODE = ord('9')
    
    #intialize bool var true
    isValid = True
    
    #iterate throught the chars in the string
    for i in range(len(strInt)):
        #determine Unicode val of this char
        charVal = ord(strInt[i])
        #if not in correct range, flip isValid to False
        if (charVal < MIN_UNICODE or charVal > MAX_UNICODE):
            isValid = False
            
    return isValid


def getValidInteger():
    """
    Implements a loop of iterate until the user enters a valid integer
    In the body of the loop
        Prompt the user to enter an integer
        Calls the isValidInteger() function to determine if this is valid numeric
        Exits the loop when valid input is obtained
    Returns the string input cast to an int
    """
    #set up boolean variable to control the loop
    isValid = False
    
    #initialize strInput
    strInput = ""
    
    while(not isValid):
        #get string input from user
        strInput = input("Enter an integer: ")
        isValid = isValidInteger(strInput)
        if (not isValid):
            print("Invalid integer was entered: try again")
            
    #after exiting the loop return strInput cast to an int
    return int(strInput)


def getRandomInts(min, maxPlusOne, numInts):
    """Assumes the follwing:
        min is an int which specifies the smallest random int to generate
        maxPlusOne is an int which specifies one more than largest random int to generate
        numInts is an int which specifies how many random ints to generate
        Returns the list of random ints
    """
    
    #start with empty list of random ints
    randInts = []
    
    #use for loop to iterate to get required number of random ints
    for i in range(numInts):
        newInt = np.random.randint(min, maxPlusOne)
        #append newint to randInts list
        randInts.append(newInt)
        
    return randInts

def gcdIterative(a, b):
    """
    Assumes a and b are ints
    implements loop to determine gcd of a and b
    Returns the gcd and numIterations required to determine this
    """
    #keep track of numIterations required
    numIterations = 0
    
    #initialize remainder to zero
    remainder = 0
    
    #implement loop to compute gcd
    while(b!=0):
        remainder = a % b
        a = b
        b = remainder
        numIterations += 1
        
        #after exiting loop return a and numIterations
    return a, numIterations

def displayListSubset(oneList, subsetSize):
    """
        Assumes oneList is a python list
        subsetSize is a positive int that specifies how many elements of the list to display
    """
    #set up a list to contain the subset
    listSubset = []
    for i in range(subsetSize + 1 ):
        listSubset.append((oneList[i]))
        
    print(listSubset)
    
def factIterative(n):
    """
        Assumes n is an int > 0
        Implements the iterative version of the algorithm
        Returns n! and the number of iterations required to compute n!
    """
    #initializes results to 1
    results = 1
    #initalizes numIterations
    numIterations = 0
    #loop to multiple each fact by previous
    while n > 1:
        results *= n
        #decrements loop
        n -= 1
        #increments iterations
        numIterations += 1 
    #returns fact num and iterations
    return results#, numIterations

def getGcdIterativesList(listA, listB):
    """
        Assumes listA and listB are equivalently sized python lists of ints
        Implements iterative gcd method to determine gcd of each pair
        Returns the following:
            execution time required
            list of gcd values
            list of num iterations required
    """
    #initialize is of gcd vals
    gcdList = []
    numIterations = []
    
    #get start time
    startTime = time.time()
    #iterate through the lists and determine gcd of each pair
    for i in range(len(listA)):
        curGcd, numIt = gcdIterative(listA[i], listB[i])
        #append this gcd to gcdList
        gcdList.append(curGcd)
        #append this numIterations to the numIterations list
        numIterations.append(numIt)
        
    endTime = time.time()
    itExeTime = endTime - startTime
    #return exe time, gcdList and numIterations list
    return gcdList


def getLines(fn):
    """Function to read a file and return a list of the lines in the file:
    Assumes fn is a string which is the name of the file
    """
        
    #open the file so that it can be read (i.e. 'r')
    nameHandle = open(fn, 'r')
    #create an empty list of lines
    lines = []
    for line in nameHandle:
        #as each line is read, append (i.e. add) this to the list
        lines.append(line)
    #dont forget to close the file...or you will have problems
    nameHandle.close()
    #return the list of lines
    return lines

def readFile(fn):
    """
        Function to read a file and display each line in the file that has been read
    """
    inFile = open(fn, 'r')
    
    for line in inFile:
        print(line)
        
    #dont forget to close the file or you will have a problem
    inFile.close()
    
def writeFile(fn, lines):
    """
        Assume fn is a string that is the name of the file to write
        Assume lines is a list of  the lines to write the file
        Writes the list of lines to file
    """
    
    #create the file handle
    outFile = open(fn, 'w')
    
    #iterate through the list of lines, appending each on to the file
    for i in range(len(lines)):
        outFile.write(lines[i])
        
    #dont forget to close the file or you will have problems!
    outFile.close()
    
def variance(nums):
    """Assumes that nums is a list of numbers."""
    mean = sum(nums) / len(nums)
    tot = 0.0
    for x in nums:
        tot += (x - mean)**2
    return tot / len(nums)

def stdDev(nums):
    """
    Assumes that nums is a list of numbers.
    Returns the standard deviation of nums
    """
    
    #the std devation is the square root of the variance
    return variance(nums)**0.5

def nChooseK(n, k):
    """Asssumes n and k are positive integers
    Computes the binomial coefficents of n and k
    Returns the number of subsets of size k than can be constructed from a set
    of size n; assumems order does not matter: i.e {1,2} and {2,1} are
    identical
    """
    #teh numerator is factorial of n
    num = factIterative(n)
    #the denominator is factorial of k times factorual of (n-k)
    den = factIterative(k) * factIterative((n-k))
    #retrun the result of integer division recall that // is integer division
    return num// den


def intMeans(totalInts, intsPerSubset, minVal, maxVal):
    """
    Assumes all four args are positive ints
    functions to get a list of means of subsets of randmon ints alyes
    the total number of ints is divided into
    subset os sizes intspersubset
    minVals: the smallest random int value
    maxVal: one more than the largest random int value
    The random ints are generated using numpy.random randInt()
    return the list of means
    """
    
    #determine how many subsets this tital number of ints can be 
    #broken up into
    numMeans = totalInts // intsPerSubset#set up an empty list for the means
    means = []
    #use nested for loop generate the subsets and determine their means
    #the outer loop is count controllled by the number of subsets
    for i in range(numMeans):
        #initialize the sim of ints in this subset to zero
        vals = 0
        #the inner loop is count controled by size of each subset
        for j in range(intsPerSubset):
            #increment vals y htis element of subset
            vals += np.random.randint(minVal, maxVal)
        #determine the mean of this subset and append to the means list
        means.append(vals/intsPerSubset)
    #return the list of means
    return means

def getMean(nums):
    """
    Assumes nums is a python list of numbers (either int or float)
    Function returns the mean valuye of the numbers in a python list
    """
    #use python built in fuction sum to compute the total of all
    #numerical values in the list 
    totalVal = sum(nums)
    #calculate teh mean by dividing totalVal by thength of the list
    meanVal = totalVal / len(nums)
    #return meanVal
    return meanVal

def formatRegressionGraph(pDegree):
    """
    Assumes pDegree is a positive int
    Returns formated line style as determined by the polynomial degree
    """
    
    if pDegree == 1:
        strFormatData = 'b--'
    elif pDegree == 2:
        strFormatData =  'c--'
    elif pDegree == 3:
        strFormatData =  'r--'
    elif pDegree == 4:
        strFormatData =  'g-'
    elif pDegree == 5:
        strFormatData =  'g--'
    else:
        strFormatData =  'm--'
        
    return strFormatData