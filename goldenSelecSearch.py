import numpy as np
import math as m

from Poly import Polynomial

'''
  'Description: A function to determine the max of a polynomial using golden selection search
  'Author: Uygur Tepe
'''

#global variable to define the golden ratio
grat = (m.sqrt(5) - 1) / 2

class Optimization(Polynomial):
    
    def __init__(self):
        super().__init__()
    
    def getBoundry(self):
        lower = float(input("Enter lower bound of where the method should star iterating: "))
        upper = float(input("Enter upper bound of where the method should star iterating: "))
        
        return lower, upper
    
    def errorCalc(self, xUpper, xLow, xOpt):
        return (1- grat)*abs((xUpper-xLow)/ xOpt) *100


    def goldSelecSort(self, xLow, xUpper, errorTol, maxIter):
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
    

def main():
    print("This will program will approximate the maximum of an inputted polynomial")
    print("Enter the information for the polynomial: ")
    degree = int(input("Enter the degree of the polynomial: "))
    terms = Optimization().getCoeffBaseX(degree)
    
    function = Optimization()
    function.setTerms(terms)
    function.displayPoly()
    xLower, xUpper = function.getBoundry()
    errorTol = function.getErrorTolerance()
    maxIter = function.maxIterations()
    
    xOpt = function.goldSelecSort(xLower, xUpper, errorTol, maxIter)
    print("xMax = " + str(xOpt) + ", FunctionValue(xMax) = " + str(function.getValue(xOpt)))
    


if __name__ == "__main__":
    main()