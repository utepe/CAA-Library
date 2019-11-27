import numpy as np

'''
  'Description: A program with takes in the terms of a polynomical and locates the roots based using 3 differnt rootfinding methods
  'Author: Uygur Tepe
'''
from Polynomial import Polynomial

class Roots(Polynomial):
    
    '''Constructor'''
    def __init__(self, *args):
        Polynomial.__init__(self, args)
    
    ''' Error calculation method
        Input: xOld, xNew
        Output: error of the new x value as a percentage
    '''
    def errorCalc(self, xOld, xNew):
        return abs((xNew-xOld)/xNew) * 100
    
    ''' Newton Raphson Method of root finding 
        Input: initial guess, xNaught, the desired error tolerace, and maximum number of iterations
        Output: approximated root of the function
    '''
    def newtonRaphsonMethod(self, xNaught, errorTolerance, maxIterations):
        xNew = 0
        error = 0
        i = 0
        
        while i < maxIterations:
            xNew = xNaught - (self.getValue(xNaught)/self.getDerivativeValue(xNaught))
            
            if i > 0:
                error = self.errorCalc(xNaught, xNew)
                if error < errorTolerance:
                    break
            
            xNaught = xNew
            i = i + 1
        
        return xNew
    
    ''' Method to get users inital guess
        Input: 
        Output: user inputted initial guess
    '''
    def getInitialGuess(self):
        xNaught = float(input("Enter the initial guess where the method should beging at: "))
        return xNaught
    
    def runRootFind(self, terms):
        self.__init__(terms)
        self.displayPoly()
        self.displayDerivative()
        xNaught = self.getInitialGuess()
        errorTol = self.getErrorTolerance()
        maxIter = self.maxIterations()
        print("A root using Newton-Raphson Method: {:0.6f} \n".format(self.newtonRaphsonMethod(xNaught, errorTol, maxIter)))

