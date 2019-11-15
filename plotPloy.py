import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

from Polynomial import Polynomial
class Plotter(Polynomial):
    
    pass


def main():
    '''
    degree = Polynomial().getInfo()
    terms = Polynomial().getCoeffBaseX(degree)
    '''
    p = Polynomial()
    
    X = np.linspace(-2, 2, 100, endpoint=True)
    Y = p(X)
    plt.plot(X, Y)
    
    plt.show()
    
    #fig.savefig("myFirstSave")

if __name__ == '__main__':
    main()

