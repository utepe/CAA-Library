import numpy as np
import math as m

from Polynomial import Polynomial

'''
    Description: A Class to determine the max of the entered polynomial using golden selection search
    Author: Uygur Tepe
'''

#global variable to define the golden ratio
grat = (m.sqrt(5) - 1) / 2

class Optimization(Polynomial):
    
    '''Constructor'''
    def __init__(self, *args):
        Polynomial.__init__(self, args)
        
    ''' Method to user defined boundries of where the search should begin iterating at
        Input:
        Output: returns lower, and upper bound x-values where iteratings will begin 
    '''
    def getBoundry(self):
        lower = float(input("Enter lower bound of where the method should start iterating: "))
        upper = float(input("Enter upper bound of where the method should start iterating: "))
        
        return lower, upper
    
    ''' Error calculation method
        Input: upper x-val, lower x-val, optimal x-val
        Output: error of the optimal x value as a percentage
    '''
    def errorCalc(self, xUpper, xLow, xOpt):
        return (1- grat)*abs((xUpper-xLow)/ xOpt) *100

    ''' Golden selection search method to approximate the max of the inputted function
        Input: lower and upper boundry x-val, desired error tolerance, maximum number of iterations
        Output: Optimal x-value where maximum is approximated to
    '''
    def goldenSearch(self, xLow, xUpper, errorTol, maxIter):
        x1 = 0
        x2 = 0
        xOpt = 0
        
        i = 0
                
        while  i < maxIter:
            x1 = xLow + grat*(xUpper-xLow)
            x2 = xUpper - grat*(xUpper-xLow)
            
            if self.poly(x1) > self.poly(x2):
                xOpt = x1
                
                xLow = x2
                x2 = x1
                x1 = xLow + grat*(xUpper-xLow)
                
            else:
                xOpt = x2
                
                xUpper = x1
                x1 = x2
                x2 = xUpper - grat*(xUpper - xLow)
            
            if(self.errorCalc(xUpper, xLow, xOpt) < errorTol):
                    break
                
            i = i + 1   
        
        return xOpt
    
    def runOptimum(self, terms):
        self.__init__(terms)
        self.displayPoly()
        xLower, xUpper = self.getBoundry()
        errorTol = self.getErrorTolerance()
        maxIter = self.maxIterations()
        xOpt = self.goldenSearch(xLower, xUpper, errorTol, maxIter)
        print("xMax = " + str(xOpt) + ", FunctionValue(xMax) = " + str(self.getValue(xOpt)) + "\n")
    