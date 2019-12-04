class Simplex:
    A = []
    B = []
    C = []
    maxZ = None
    numVar = None
    constaintNum = None
    column = None
    row  = None
    
    def __init__(self):
        self.A = []
        self.B = []
        self.C = []
        self.maxZ = 0
    
    def setSizes(self):
        self.numVar = int(input("Enter the number of Variables that need to be optimized: "))
        self.constaintNum = int(input("Enter the number of constraints: "))
        self.column = self.constaintNum + self.numVar
        self.row = self.constaintNum
    
    def setVariableMat(self):
        self.setSizes()
        
        cVar = list(map(float, input("Enter the coefficients of the variables of the function we are maximizing (seperate coeffs with a space): \n").split()))
        
        self.C = cVar.copy()
        i = len(cVar)
        while i < self.column:
            self.C.append(0)
            i += 1
        
        self.B = list(map(float, input("Enter the values of the constaints (separate values with a space): \n").split()))
            
        row = []
        for j in range(self.row):
            row = list(map(float, input("Enter the coefficient of constaint eqn " + str(j+1) + " with the slack variable coefficients (seperate coeffs with a space): \n").split()))
            self.A.append(row)
        
        print("\nInital non-optimal Array: ")
        self.displayCurrent()
        
    def simplexAlg(self):
        run = self.isOptimum()
        
        while run == False:
            run = self.doSimplexCalc()
           
        print("\nDetermined Optimized Array and Values: ")
        self.displayCurrent()
        self.findMax()
        
    def isOptimum(self):
        for i in self.C:
            if i > 0.0:
                return False
        
        return True
    
    def doSimplexCalc(self):
        if self.isOptimum():
            return True
        
        pivotColumn = self.findPivotColumn()
        pivotRow = self.findSmallestB(pivotColumn)
        self.doRowOperations(pivotColumn, pivotRow)
        return False
    
    def findPivotColumn(self):
        return self.C.index(max(self.C))
    
    def findSmallestB(self, pivotColumn):
        positiveValues = [0] * self.row
        results = [0] * self.row
        
        for i in range(self.row):
            if self.A[i][pivotColumn] > 0:
                positiveValues[i] = self.A[i][pivotColumn]
            
        for i in range(self.row):
            value = positiveValues[i]
            if value > 0:
                results[i] = self.B[i]/value
            else:
                results[i] = 99999999
                
        return results.index(min(results))
    
    def doRowOperations(self, pivotColumn, pivotRow):
        pivotMultiplier = self.A[pivotRow][pivotColumn]
        self.maxZ -= ((self.C[pivotColumn] * self.B[pivotRow]) / pivotMultiplier)
        pivotRowValue = [0] * self.column
        pivotColumnValue = [0] * self.row
        newRow = [0] * self.column
        
        for i in range(self.column):
            pivotRowValue[i] = self.A[pivotRow][i]
            newRow[i] = pivotRowValue[i] / pivotMultiplier
            
        for i in range(self.row):
            pivotColumnValue[i] = self.A[i][pivotColumn]
        
        self.B[pivotRow] /= pivotMultiplier
        
        for i in range(self.row):
            if(i != pivotRow):
                for j in range(self.column):
                    multiplier = pivotColumnValue[i]
                    self.A[i][j] -= multiplier * newRow[j]
        
        for i in range(self.row):
            if(i != pivotRow):
                multiplier = pivotColumnValue[i]
                self.B[i] -= multiplier * self.B[pivotRow]
        
        multiplier = self.C[pivotColumn]
        for i in range(self.column):
            self.C[i] -= multiplier * newRow[i]
            
        for i in range(self.column):
            self.A[pivotRow][i] = newRow[i]
        
    def displayCurrent(self):
        for i in self.A:
            print(i)     
    
    def findMax(self):
        print("Values of the constrained variables are: ")
        counter = 0
        flag = False
        coeffB = []
        
        for i in range(self.column):
            if flag == True:
                break
            for j in range(self.row):
                if self.A[j][i] == 1:
                    coeffB.append(self.B[j])
                    counter += 1
                    if counter == self.numVar:
                        flag = True
                        break
    
        for i in coeffB:
            print("X" + str(coeffB.index(i)) + ": " + str(i))
            
        print("\nOptimized Max Value is " + str(abs(self.maxZ)))
        
    def runSimplex(self):
        self.setVariableMat()
        self.simplexAlg()
    