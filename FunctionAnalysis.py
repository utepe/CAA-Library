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
        print("[1] Enter a new Polynomial")
        print("[2] Find the a root of the function")
        print("[3] Find the max/min value of the function (Optimum)")
        print("[4] Plot the given function for a graphical solution")
        print("[5] Find the integral of the given function")

        return int(input("\nEnter what you would like to do: "))
    
    def methodSelector(self, choice, terms):
        selector = {
            2 : Roots().runRootFind,
            3 : Optimize().runMinMaxFind,
            4 : Plotter().runPlotter,
            5 : Integrals().runFindIntegral,
        }
        
        selector[choice](terms)
    
    def runPolyAnalysis(self):
        print("\nPolynomial Analysis Menu")
        print("----------------------------")
        key = int(input("If you would like to stay on this page, enter [1]: "))
        if key == 1:
            degree = self.setDegree()
            terms = self.setCoeffBaseX(degree)
            flag = False
            while flag == False:
                choice  = self.getChoice()
                if choice == 0:
                    print("Going back to the main menu")
                    break
                elif choice == 1:
                    degree = self.setDegree()
                    terms = self.setCoeffBaseX(degree)
                else:
                    self.methodSelector(choice, terms)
        else: 
            return
            