
from goldenSelecSearch import Optimization
from rootFinding import Roots
from plotPloy import Plotter
from optimize import Optimize

class Selection:
    def __init__(self):
        pass
    
    def methodSelector(self, choice, terms):
        selector = {
            1 : Roots().runRootFind,
            2 : Optimize().runMinMaxFind,
            3 : Plotter().runPlotter, 
        }
        
        selector[choice](terms)