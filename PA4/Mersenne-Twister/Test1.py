# Runs Test for testing randomness of data.

import math
import statistics
from main import Mersenne
  
def runsTest(l, l_median):
    runs, n1, n2 = 0, 0, 0
    # Checking for start of new run
    for i in range(len(l)):
        if (l[i] >= l_median and l[i-1] < l_median) or (l[i] < l_median and l[i-1] >= l_median):      # no. of runs
            runs += 1  
          
        if(l[i]) >= l_median:                                                                         # no. of positive values
            n1 += 1   
        
        else:                                                                                           # no. of negative values
            n2 += 1   
  
    runs_exp = ((2 * n1 * n2) / (n1 + n2)) + 1
    stan_dev = math.sqrt((2 * n1 * n2 * (2 * n1 * n2 - n1 - n2))/ (((n1 + n2) ** 2) * (n1 + n2 - 1)))
    return (runs - runs_exp) / stan_dev
    
def main():
    print("---------RUNS_TEST-----------")
    l = []
    Z_critical_95_confidence = 1.96
    Seed = 0
    NUMBER_OF_SAMPLES = 10**4
    Rand = Mersenne(Seed)
    for i in range(NUMBER_OF_SAMPLES):
        l.append(Rand.random())
          
    l_median= statistics.median(l)
    Z = abs(runsTest(l, l_median))
    print("Z_critical: ", Z_critical_95_confidence)
    print("Z-statistic: ", Z)

    if(Z < Z_critical_95_confidence):
        print("Fail To Reject null hypothesis")
    else:
        print("Reject null hypothesis")


if __name__ == '__main__':
    main()