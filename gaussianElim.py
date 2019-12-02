class GaussElim:
    matrix = []
    size = None
    soln = []
    
    def __init__(self):
        pass
    
    def getSize(self):
        '''Sets the size of the matrix''' 
        self.size = int(input("Enter the size of the matrix you would like to solve: "))
        
    def setMat(self):
        '''Sets the matrix that is to be solved'''
        row = []
        print("\nEnter the coefficents of the terms in each row: ")
        for i in range(self.size):
            row = list(map(float, input("Row " + str(i+1) + " (seperate coeffs with a space): \n").split()))
            self.matrix.append(row)
        
        print("\nEntered Matrix is: ")
        self.displayMat()
        
    def displayMat(self):
        '''Method to display the Matrix'''
        for i in self.matrix:
            print(i)
     
    def potentialPivot(self):
        '''
        Method that checks if the first coefficeint of the matrix is 0
        If coeff is 0, removes first equation and appends it to the end of the system
        '''
        while self.matrix[0][0] == 0:   #repeats process until first coefficient is not 0
            temp = self.matrix.pop(0)
            self.matrix.append(temp)
           
    def solveMat(self):
        '''Solve System of Linear Equations using Gaussian Elimination'''
        self.potentialPivot()           #calls potential pivot method
        column = len(self.matrix[0])    #sets column to the length of 1 equation
        self.soln = [0] * self.size     #initialize the solution list to Zeros
        
        for h in range(self.size):
            divisor = self.matrix[h][h]
            i = h + 1
            while i < self.size:        # do triangular reduction
                factor = self.matrix[i][h] / divisor
                for j in range(column):
                    self.matrix[i][j] -= factor * self.matrix[h][j]
                i += 1
            
            k = self.size - 1
            while k >= 0:               #do back subsitution, solve for unknowns
                l = k + 1
                self.soln[k] = self.matrix[k][column - 1]
                while l < self.size:
                    self.soln[k] -= self.matrix[k][l] * self.soln[l]
                    l += 1
                self.soln[k] /= self.matrix[k][k]
                k -= 1
                
    def displaySoln(self):
        '''
        Calls Solve Mat Method
        Displays the solved matrix
        Displays the solutions to the unknowns
        '''
        self.solveMat()
        print("\nSolved Matrix is: ")
        self.displayMat()
        
        print("Solutions to the unknowns are:")
        for i in range(len(self.soln)):
            print("X" + str(i+1) + " = " + str(self.soln[i])) 
        
    def runGaussElim(self):
        self.getSize()
        self.setMat()    
        self.displaySoln()
            