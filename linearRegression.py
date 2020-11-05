import numpy as np
import matplotlib.pyplot as plt
import math as m

class linearRegress():
    lineEqn = np.poly1d([])
    X = []
    Y = []
    N = None
    sumX = 0
    sumY = 0
    sumXY = 0
    sumX2 = 0
    slope = None
    yInt = None
    sR = 0
    sXY = None
    r = None
    
    def __init__(self):
        pass
        
    def setN(self):
        '''Setter Method for number of data points'''
        self.N = int(input("Enter the number of Data Points: "))
    
    def setTerms(self):
        '''Setter method for the terms'''
        self.setN()
        for i in range(self.N):
            self.X.append(float(input("X" + str(i) + ": ")))
            self.Y.append(float(input("Y" + str(i) + ": ")))
        
    def findSummations(self):
        '''Method to find the summations for each terms in the least sqaures method'''
        for i in range(self.N):
           self.sumX += self.X[i]
           self.sumY += self.Y[i]
           self.sumXY += self.X[i] * self.Y[i]
           self.sumX2 += m.pow(self.X[i], 2)
    
    def findLineEqn(self):
        '''Finds the slope an yInter of the data points using least sqaure method'''
        self.findSummations()
        self.slope = ((self.N * self.sumXY - self.sumX * self.sumY) / (self.N * self.sumX2 - m.pow(self.sumX, 2)))
        self.yInt = ((self.sumY - self.slope * self.sumX) / self.N)
        self.lineEqn = np.poly1d([self.slope, self.yInt])
        
        print("\nEquation of the line of best fit is: " + str(self.lineEqn))
        
    def findStdError(self):
        '''Finds the Standard Error in the line'''
        for i in range(self.N):
            self.sR += m.pow((self.Y[i] - self.yInt - self.slope * self.X[i]), 2)
            
        self.sXY = m.sqrt(self.sR / (self.N - 2))
        
        print("The standard error in the line is: {:0.6f}".format(self.sXY))
        
    def findR(self):
        yBar = self.sumY / self.N
        sT = 0
        for i in range(self.N):
            sT += m.pow((self.Y[i] - yBar), 2)
        
        self.r = m.sqrt((sT - self.sR) / sT)
    
    def plotLine(self):
        '''Plots the line of best fit against the scattered data points'''
        plt.scatter(self.X, self.Y, s =10)
        x = np.linspace((self.X[0] - 2), (self.X[self.N-1] + 2), 100, endpoint=False)
        y = self.lineEqn(x)
        plt.title("Data Points w/ Line of Best Fit")
        plt.xlabel("X-Axis")
        plt.ylabel("Y-Axis")
        plt.grid(True)
        setLabel = ("Line of Best Fit \nR^2 = {:0.6f}".format(m.pow(self.r, 2)))
        linePlt = plt.plot(x, y, label = setLabel)
        plt.legend()
        plt.show()
        
    def runLineFit(self):
        print("Linear Regression Menu")
        print("-------------------------")
        key = int(input("If you would like to stay on this page, enter [1]: "))
        if key == 1:
            self.setTerms()
            self.findLineEqn()
            self.findStdError()
            self.findR()
            self.plotLine()
        else:
            print("Going back to the main menu")
            
