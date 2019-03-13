author__ = "Michael Bristol"
__copyright__ = "Copyright 2019, Modelling and Simulation"
__credits__ = ["Michael Bristol"]
#Shaft radius 1.00cm
#Distribution radii 1.00cm mean
#Standard Distribution .002cm
#Triangular distribution mode 1.00cm maximum difference of 0.003

import numpy as np
def get_Triangular(left,mode,right):
    return np.random.triangular(1-left,mode,1+right)
