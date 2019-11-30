from FunctionAnalysis import polyAnalysis
from linearRegression import linearRegress

def getChoice():
    print("\nWhat would you like to do with this program?")
    print("[0] Terminate Program")
    print("[1] Input a Polynomial and Analyze it")
    print("[2] Find the equation for a Line of Best Fit")
    #print("[3] Solve Matricies and Linear Algebra Related Problems") WIP
    
    return int(input("\nEnter what you would like to do: "))

def programSelector(choice):
    selector = {
        1 : polyAnalysis().runPolyAnalysis,
        2 : linearRegress().runLineFit,
        }
    
    selector[choice]()
    
def main():
    flag = False
    while flag == False:
        key = getChoice()
        if key == 0:
            flag = True
        else:
            programSelector(key)
    
    
if __name__ == '__main__':
    main()
    