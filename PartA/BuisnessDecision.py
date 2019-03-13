# 1 billion bushing shafts
# each failure costs 5000
# reducing sd by 0.0005 costs 100,000
# reduce Max difference by 0.001 costs 500,000

import numpy as np


from MonteCarlo import interfer_Probab


def regular_failure_cost(runs, cost):
    return (interfer_Probab(runs, 0.003, 1, 0.003, 1, 0.002)*runs)*cost


def reducing_SD(runs, cost, ReduceSD):
    return ((interfer_Probab(runs, 0.003, 1, 0.003, 1, (0.002-ReduceSD))*runs)*5000)+cost

# print ('Regular Failure Costs:', interfer_Probab(
#     1000000, 0.003, 1, 0.003, 1, 0.002))


def reducing_Max(runs, cost, reduceMaxDifference):
    return ((interfer_Probab(runs, 0.003, 1, (0.003-reduceMaxDifference), 1, (0.002))*runs)*5000)+cost


def best_decision():
    l = []
    r = regular_failure_cost(1000000, 5000)
    rsd = reducing_SD(1000000, 100000, 0.0005)
    rmd = reducing_Max(1000000, 500000, 0.001)
    print("Regular failure costs", r)
    print("Reducing standard deviation", rsd)
    print("Reduce Max Difference", rmd)
    # l.append(regular_failure_cost(1000000, 5000))
    l.append(r)
    l.append(rsd)
    l.append(rmd)
    x = min(float(s) for s in l)
    return x


print("The Best Business Decision is", best_decision())
