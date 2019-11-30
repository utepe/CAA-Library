from Polynomial import Polynomial
from rootFinding import Roots
from plotPloy import Plotter
from optimize import Optimize
from integration import Integrals

class polyAnalysis(Polynomial):
    
    def __init__(self):
        pass
       
    def getChoice(self):
        print("\nWhat would you like to do with this function?")
        print("[0] Return to Main Menu")
        print("[1] Find the a root of the function")
        print("[2] Find the max/min value of the function (Optimum)")
        print("[3] Plot the given function for a graphical solution")
        print("[4] Find the integral of the given function")

        return int(input("\nEnter what you would like to do: "))
    
    def methodSelector(self, choice, terms):
        selector = {
            1 : Roots().runRootFind,
            2 : Optimize().runMinMaxFind,
            3 : Plotter().runPlotter,
            4 : Integrals().runFindIntegral,
        }
        
        selector[choice](terms)
    
    def runPolyAnalysis(self):
        degree = self.getInfo()
        terms = self.getCoeffBaseX(degree)
        flag = False
        while flag == False:
            choice  = self.getChoice()
            if choice == 0:
                break
            self.methodSelector(choice, terms)
        