### 1st question

import numpy as np
import scipy.stats as stats #This library will be used to calculate the Empyrical CDF.
import matplotlib.pyplot as plt
## The mathematical part is on the relatory, specifically on the part that adresses this
#exercise.

## We can simulate Y and Z via Inversion Method, by whick we can obtain that t = sqrt(u), u
#being one observation of an uniform in ]0,1[. Therefore,

def simulate_Y_and_Z(samSize):
    sample = [ ]
    
    for i in range(samSize):
        unif = np.random.rand()

        elem = np.sqrt(unif)
        sample.append(elem)

    return(sample)

sim_Y = simulate_Y_and_Z(1000)
sim_Z = simulate_Y_and_Z(1000)

## Histogram comparing the distributions:

plt.figure()
plt.hist(sim_Y, color='blue', edgecolor='black', label='Dist.Maximum')
plt.hist(sim_Z, color='black', edgecolor='black', alpha=0.6, label='Dist.Sqrt')
plt.title('Histogram of the observations obtained by the simulations of Y (maximum) and Z (square-root).')
plt.xlabel('Observed values')
plt.ylabel('Abs. frequency')
plt.legend()

#

## A plot that compares the analytical and empyrical CDF's:

empyricalCDF = stats.ecdf(sim_Y).cdf
analyticalCDF = np.square(sorted(sim_Y))

plt.figure()
plt.plot(sorted(sim_Y), analyticalCDF, color='darkgreen', label='Analytical CDF')
plt.plot(empyricalCDF.quantiles, empyricalCDF.probabilities, color='red', label='Empyrical CDF')
plt.xlabel('Values (analytical CDF) and quantiles (empyrical CDF)')
plt.ylabel('Cumulative Density')
plt.legend()

plt.show 
