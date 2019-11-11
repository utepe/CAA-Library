import numpy as np

'''
  'Description: A program with takes in the terms of a polynomical and locates the roots based using 3 differnt rootfinding methods
  'Author: Uygur Tepe
'''
from Poly import Polynomial

class Roots(Polynomial):
    
    def errorCalc(self, xOld, xNew):
        return abs((xNew-xOld)/xNew) * 100
    
    def bisectionMethod(self, xLow, xHigh, errorTolerance, maxIterations):
        
        xNew = 0
        xOld = 0
        error = 0
        i = 0
        
        while i < maxIterations:
            xNew = (xLow + xHigh) / 2
            
            if xNew == 0:
                return xNew
            elif self.getValue(xNew)*self.getValue(xLow) < 0:
                xHigh = xNew
            elif self.getValue(xNew)*self.getValue(xLow) > 0:
                xLow = xNew
            
            if i > 0:
                error = self.errorCalc(xOld, xNew)
                if error < errorTolerance:
                    break
            
            xOld = xNew
            i = i + 1
        
        return xNew
        
    def faslePositionMethod(self, xLow, xHigh, errorTolerance, maxIterations):
        
        xNew = 0
        xOld = 0
        error = 0
        i = 0
        
        while i < maxIterations:
            xNew = xHigh - (self.getValue(xHigh)*(xLow-xHigh)/(self.getValue(xLow)-self.getValue(xHigh)))
            
            if self.getValue(xNew)*self.getValue(xLow) <= 0:
                xHigh = xNew
            else:
                xLow = xNew
            
            if i > 0:
                error = self.errorCalc(xOld, xNew)
                if error < errorTolerance:
                    break
            
            xOld = xNew
            i = i + 1
        
        return xNew
    
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
    
    def getValue(self, xValue):
        return self.poly(xValue)
        
def main():
    print("Enter the information for the polynomial: ")
    degree = int(input("Enter the degree of the polynomial: "))
    terms = Polynomial().getCoeffBaseX(degree)
    
    initial = Polynomial()
    initial.setTerms(terms)
    initial.displayPoly()
    initial.displayDerivative()
    errorTol = function.getErrorTolerance()
    maxIter = function.maxIterations()

    print("")
    
    print("Bisection Method: {:0.6f}".format(initial.bisectionMethod(3, 5, errorTol, maxIter)))
    print("-------------------------------------------")
    print("False Position Method: {:0.6f}".format(initial.faslePositionMethod(3, 5,errorTol, maxIter)))
    print("-------------------------------------------")
    print("Newton-Raphson Method: {:0.6f}".format(initial.newtonRaphsonMethod(5, errorTol, maxIter)))
         

if __name__ == '__main__':
    main()