
import numpy as np

'''
    Description: Base Class for most Programs that use Polynomials in the Project Library
    Author: Uygur Tepe
'''

class Polynomial:
    poly = np.poly1d([])
    polyDerivative = np.polyder(poly)

    def __init__(self, *args):
        degree = self.getInfo()
        terms = self.getCoeffBaseX(degree)
        #args = np.array(args).reshape([-1])
        self.poly = np.poly1d(terms)
        self.polyDerivative = np.polyder(self.poly)
        pass
    
    def __call__(self, x):
        return self.poly(x)
    
    ''' Update: This is no longer necessary (redundant)
    def setTerms(self, terms):
        self.poly = np.poly1d(terms)
        self.polyDerivative = np.polyder(self.poly)
    '''
       
    def displayPoly(self):
        print("You entered polynomial: ")
        print(self.poly)
        
    def displayDerivative(self):
        print("It's derivative: ")
        print(self.polyDerivative)

    def getCoeffBaseX(self, degree):
        polyCoeff = []
        
        count = 0
        while count <= degree:
            
            eachCeoff = float(input("Enter the coefficient for term  x^" + str(degree - count) + ": "))
            polyCoeff.append(eachCeoff)

            count = count + 1
        
        return polyCoeff
    
    def getValue(self, xValue):
        return self.poly(xValue)
    
    def getDerivativeValue(self, xValue):
        return self.polyDerivative(xValue)
    
    def getErrorTolerance(self):
        errorTol = float(input("Enter the desired error tolerance (%): "))
        return errorTol
    
    def maxIterations(self):
        maxIter = float(input("Enter the desired amount of iterations: "))
        return maxIter
    
    def getInfo(self):
        print("Enter the information for the polynomial: ")
        degree = int(input("Enter the degree of the polynomial: "))
        return degree