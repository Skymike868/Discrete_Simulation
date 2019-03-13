#Shaft radius 1.00cm
#Distribution radii 1.00cm mean
#Standard Distribution .002cm
#Triangular distribution mode 1.00cm maximum difference of 0.003

import numpy as np
#Bushing manufactoring
def get_Triangular(left,mode,right):
    return np.random.triangular(1-left,mode,1+right)

def get_Shaft(radius, sd):
    return np.random.normal(radius,sd)


def interfer_Probab(runs):
    C=0
    for count in range(1,runs):
        x=(get_Triangular(0.003,1,0.003))
        y=(get_Shaft(1,.002))
        if x<y:
            C=C+1
         
    print(runs)
    print(C)
    e=C/runs
    print (e)
    return C/runs

print ('%.2f'%interfer_Probab(10000))

# print (get_Triangular(0.003,1,0.003))
# print(get_Shaft(1,.002))


    



