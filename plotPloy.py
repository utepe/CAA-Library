import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from Polynomial import Polynomial

class Plotter(Polynomial):
    def __init__(self, *args):
        Polynomial.__init__(self, args)
        
    ''' set domain'''
    def setDomain(self):
        print("\nEnter the domain of the where the function should be plotted along the x-axis")
        lowerBound = float(input("Enter the Lower Bound of the function: "))
        upperBound = float(input("Enter the Upper Bound of the function: "))
        return lowerBound, upperBound

    def setXY(self, poly):
        lowerX, upperX = self.setDomain()
        X = np.linspace(lowerX, upperX, 100, endpoint=True)
        Y = poly(X)
        return X, Y
    
    def displayPlot(self, poly):
        X, Y =  self.setXY(poly)
        plt.title("Plot of the Polynomial")
        plt.xlabel("X - Axis")
        plt.ylabel("Y- Axis")
        plt.grid(True)
        plt.plot(X, Y)
        plt.show()
    
    def runPlotter(self, terms):
        self.__init__(terms)
        self.displayPlot(self.poly)

