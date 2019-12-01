from gaussianElim import GaussElim

class linAlgAnalysis():
    
    def __init__(self):
        pass
       
    def getChoice(self):
        print("\nWhat would you like to do?")
        print("[0] Return to Main Menu")
        print("[1] Solve System of Linear Equation")
        #print("[2] Solve a constrained optimization problem") WIP

        return int(input("\nEnter what you would like to do: "))
    
    def methodSelector(self, choice):
        selector = {
            1 : GaussElim().runGaussElim,
        }
        
        selector[choice]()
    
    def runLinAlgAnalysis(self):
        while True:
            choice  = self.getChoice()
            if choice == 0:
                break
            self.methodSelector(choice)
        