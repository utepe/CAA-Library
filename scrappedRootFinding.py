'''
    Python code of other root finding methods
'''

def bisectionMethod(self, xLow, xHigh, errorTolerance, maxIterations):
        
        xNew = 0
        xOld = 0
        error = 0
        i = 0
        
        while i < maxIterations:
            xNew = (xLow + xHigh) / 2
            
            if xNew == 0:
                return xNew
            elif self.getValue(xNew)*self.getValue(xLow) < 0:
                xHigh = xNew
            elif self.getValue(xNew)*self.getValue(xLow) > 0:
                xLow = xNew
            
            if i > 0:
                error = self.errorCalc(xOld, xNew)
                if error < errorTolerance:
                    break
            
            xOld = xNew
            i = i + 1
        
        return xNew
        
def faslePositionMethod(self, xLow, xHigh, errorTolerance, maxIterations):
        
    xNew = 0
    xOld = 0
    error = 0
    i = 0
        
    while i < maxIterations:
        xNew = xHigh - (self.getValue(xHigh)*(xLow-xHigh)/(self.getValue(xLow)-self.getValue(xHigh)))
            
        if self.getValue(xNew)*self.getValue(xLow) <= 0:
            xHigh = xNew
        else:
            xLow = xNew
            
        if i > 0:
            error = self.errorCalc(xOld, xNew)
        if error < errorTolerance:
            
        xOld = xNew
        i = i + 1
        
    return xNew
    