import scipy.integrate as integrate
import numpy as np
from Polynomial import Polynomial


class Integrals(Polynomial):
    
    def __init__(self, *args):
        super().__init__(args)
        
    def setBounds(self):
        '''
        Method to get the interval of integration
        Returns: the upper and low bound of the interval
        '''
        xLow = float(input("Enter the lower bound to calcualte the definite integral: "))
        xHigh = float(input("Enter the upper bound to calcualte the definite integral: "))
        return xLow, xHigh

    def riemannSum(self, a, b):
        ''' 
        Reimman Sum Method of approximating the definite integral
        Computes over the interval [a, b] using midpoints
        '''
        n = int(10e+6)
        dx = float((b-a)/n) 
        x = np.linspace(a, b, n + 1)
        xMid = (x[:-1] + x[1:])/2
        print("\nDefinite Integral of this Polynomial using Riemann Sums is: ")
        print(np.sum(self.getValue(xMid)) * dx)
    
    def getDefIntegral(self, a, b):
        '''
        Method to get the definite integral of a polynomial 
        Using built in SciPy method
        '''
        print("\nIntegral using SciPy is (integral, error): ")
        print(integrate.quad(self.poly, a, b))        
        
    def runFindIntegral(self, terms):
        self.__init__(terms)
        self.displayPoly()
        self.displayIntegral()
        a, b = self.setBounds()
        self.getDefIntegral(a, b)
        self.riemannSum(a, b)
