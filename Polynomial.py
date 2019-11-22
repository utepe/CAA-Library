
import numpy as np

'''
    Description: Base Class for most Programs that use Polynomials in the Project Library
    Author: Uygur Tepe
'''

class Polynomial:
    poly = np.poly1d([])
    polyDerivative = np.polyder(poly)
    polySecondDer = np.polyder(polyDerivative)

    def __init__(self, terms):
        terms = np.array(terms).reshape([-1])
        self.poly = np.poly1d(terms)
        self.polyDerivative = np.polyder(self.poly)
        self.polySecondDer = np.polyder(self.polyDerivative)
        pass
    
    def __call__(self, x):
        return self.poly(x)
       
    def displayPoly(self):
        print("You entered polynomial: ")
        print(self.poly)
        
    def displayDerivative(self):
        print("It's derivative: ")
        print(self.polyDerivative)

    def displaySecondDerivative(self):
        print("It's Second Derivative")
        print(self.polySecondDer)
        
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
    
    def getSecondDerivativeVal(self, xVaue):
        return self.polySecondDer(xVaue)
    
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