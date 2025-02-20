### 3rd question 

import numpy as np
import matplotlib.pyplot as plt
## In this case, we're simulating 3 specific exponentials, but I preffered to make a more general program and, then, applicate it.

def SimulateMinExp(rates, samSize=1):
    sample = [ ]

    for i in range(samSize):
        unif = np.random.rand()
        
        elem = -np.log(1-unif)/np.sum(rates)
        sample.append(elem)

    return(sample)

testeSim = SimulateMinExp([1, 2, 3])

## This includes the program asked in the first item.

sim_Min = SimulateMinExp([1,2,3], 1000)

#

x = [i/1200 for i in range(1200)]

theoObs = [(1 + 2 + 3)*np.e**(-(1+2+3)*i) for i in x]

plt.hist(sim_Min, color='darkblue', bins=40, edgecolor='black', density=True, label='Simulated Dist. Min.')
plt.plot(x, theoObs, color='red', label='Analytical Dist. Min.')


plt.show()
