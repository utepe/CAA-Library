class GaussElim:
    matrix = []
    size = None
    soln = []
    
    def __init__(self):
        pass
    
    def getSize(self): 
        self.size = int(input("Enter the size of the matrix you would like to solve: "))
        
    def getMat(self):
        row = []
        print("\nEnter the coefficents of the terms in each row: ")
        for i in range(self.size):
            row = list(map(float, input("Row " + str(i+1) + " (seperate coeffs with a space): \n").split()))
            self.matrix.append(row)
        
        print("\nEntered Matrix is: ")
        self.displayMat()
        
    def displayMat(self):
        for i in self.matrix:
            print(i)
     
    #add swap function so first element is not 0
    def potentialPivot(self):
        if self.matrix[0][0] == 0:
            temp = self.matrix.pop(0)
            self.matrix.append(temp)
           
    def solveMat(self):
        self.potentialPivot()
        b = []
        for i in self.matrix:
            b.append(i[len(i)-1])
        
        self.soln = b
        column = len(self.matrix[0])
        
        for h in range(self.size):
            divisor = self.matrix[h][h]
            i = h + 1
            while i < self.size:
                factor = self.matrix[i][h] / divisor
                for j in range(column):
                    self.matrix[i][j] -= factor * self.matrix[h][j]
                i += 1
            
            k = self.size - 1
            while k >= 0:
                l = k + 1
                self.soln[k] = self.matrix[k][column - 1]
                while l < self.size:
                    self.soln[k] -= self.matrix[k][l] * self.soln[l]
                    l += 1
                self.soln[k] /= self.matrix[k][k]
                k -= 1
                
    def displaySoln(self):
        self.solveMat()
        print("\nSolved Matrix is: ")
        self.displayMat()
        
        print("Solutions to the unknowns are:")
        for i in range(len(self.soln)):
            print("X" + str(i+1) + " = " + str(self.soln[i])) 
        
    def runGaussElim(self):
        self.getSize()
        self.getMat()    
        self.displaySoln()
            