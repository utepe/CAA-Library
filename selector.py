from rootFinding import Roots
from plotPloy import Plotter
from optimize import Optimize
from integration import Integrals

class Selection:
    def __init__(self):
        pass
    
    def methodSelector(self, choice, terms):
        selector = {
            1 : Roots().runRootFind,
            2 : Optimize().runMinMaxFind,
            3 : Plotter().runPlotter,
            4 : Integrals().runFindIntegral,
        }
        
        selector[choice](terms)