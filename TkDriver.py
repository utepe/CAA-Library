import tkinter as tk
from tkinter import ttk
from FunctionAnalysis import polyAnalysis
from linearRegression import linearRegress
from linearAlgAnalysis import linAlgAnalysis

def getChoice():
    print("\nCAA Library Main Menu")
    print("------------------------")
    print("[0] Terminate Program")
    print("[1] Input a Polynomial and Analyze it")
    print("[2] Find the equation for a Line of Best Fit")
    print("[3] Solve Matricies and Linear Algebra Related Problems")    #WIP
    
    return int(input("\nEnter what you would like to do: "))

def programSelector():
    selector = {
        1 : polyAnalysis().runPolyAnalysis,
        2 : linearRegress().runLineFit,
        3 : linAlgAnalysis().runLinAlgAnalysis,
        }
    
    selector[choice.get()]()

root  = tk.Tk()
choice = tk.IntVar()
choiceLabel = ttk.Label(root, text = "Choice: ").pack(side = 'left')
choiceEntry = ttk.Entry(root, width = 15, textvariable = choice).pack(side = 'left')
# choiceEntry.focus()
    
choiceButton = ttk.Button(root, text = "Choose", command = programSelector).pack(side = 'left')
root.mainloop()

'''   
def main():
    
    while True:
        key = getChoice()
        if key == 0:
            break
        else:
            programSelector(key)

    
    
if __name__ == '__main__':
    main()
'''    