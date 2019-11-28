import numpy as np
import math as m

from Polynomial import Polynomial

class Optimize(Polynomial):
    
    def __init__(self, *args):
        '''Constructor'''
        Polynomial.__init__(self, args)
        
    def errorCalc(self, xOld, xNew):
        ''' 
        Error calculation method
        Input: xOld, xNew
        Output: error of the new x value as a percentage
        '''
        return abs((xNew-xOld)/xNew) * 100
    
    def secondDerNewtonRaphsonMethod(self, xNaught, errorTolerance, maxIterations):
        ''' 
        Newton Raphson Method of Min/Max finding 
        Input: initial guess, xNaught, the desired error tolerace, and maximum number of iterations
        Output: approximated root of the function
        '''
        xNew = 0
        error = 0
        i = 0
        
        while i < maxIterations:
            xNew = xNaught - (self.getDerivativeValue(xNaught)/self.getSecondDerivativeVal(xNaught))
            
            if i > 0:
                error = self.errorCalc(xNaught, xNew)
                if error < errorTolerance:
                    break
            
            xNaught = xNew
            i = i + 1
        
        return xNew
    
    def isMinMax(self, xValue):
        '''
        Method to determine wheather or not the X position found is a Maximum or Minimum
        '''
        if(self.getSecondDerivativeVal(xValue) > 0):
            print("Minimum was found at {:0.6f} \n".format(xValue))
        else:
            print("Maximum was found at {:0.6f} \n".format(xValue))
    
    def getInitialGuess(self):
        ''' 
        Method to get users inital guess
        Return: user inputted initial guess
        '''
        xNaught = float(input("Enter the initial guess where the method should beging at: "))
        return xNaught
    
    def runMinMaxFind(self, terms):
        self.__init__(terms)
        self.displayPoly()
        self.displayDerivative()
        self.displaySecondDerivative()
        xNaught = self.getInitialGuess()
        errorTol = self.getErrorTolerance()
        maxIter = self.maxIterations()
        xCalc = self.secondDerNewtonRaphsonMethod(xNaught, errorTol, maxIter)
        self.isMinMax(xCalc)