from Polynomial import Polynomial
from selector import Selection
from rootFinding import Roots
from plotPloy import Plotter
from optimize import Optimize
from integration import Integrals

class Analysis(Polynomial):
    def __init__(self, *args):
        pass
       
    def getChoice(self):
        print("\nWhat would you like to do with this function?")
        print("[0] To terminate program")
        print("[1] Find the a root of the function")
        print("[2] Find the max/min value of the function (Optimum)")
        print("[3] Plot the given function for a graphical solution")
        print("[4] Find the integral of the given function")

        print("")
        choice = int(input("Enter what you would like to do: "))
        
        return choice
    
    def methodSelector(self, choice, terms):
        selector = {
            1 : Roots().runRootFind,
            2 : Optimize().runMinMaxFind,
            3 : Plotter().runPlotter,
            4 : Integrals().runFindIntegral,
        }
        
        selector[choice](terms)
    
def main():
    function = Analysis()
    degree = function.getInfo()
    terms = function.getCoeffBaseX(degree)
    flag = False
    while flag == False:
        choice  = function.getChoice()
        if choice  == 0:
            break
        run = function.methodSelector(choice, terms)
        
if __name__ == '__main__':
    main()