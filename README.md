# Simulation-and-Monte-Carlo


## Introduction

  This project has been developed with the intent to analyze various problems, which solutions should involve various methods that were exposed and discussed in the 
classes of the discipline throughout the semester. With that in mind, most of the work was done in the most pedagogically pertinent way, avoiding the use of many libraries 
available in Python that would make all the methodology present in the solutions entirely implicit.
  

## Exercise 1:

  The idea here was to show the similarity of the distributions of the maximum of two independent uniform variables with support between 0 and 1 and the square root 
of another of those independent variables:

- First, we get that:
    P(Z <= t) = P(sqrt(X_3) <= t) = P(X_3 <= t²) (elevating both sides by 2)
                                  = t² (P(U <= u), U ~ Unif]0,1[, is u).

  Additionally, 
    
    P(max(X_1, X_2) <= t) = P(X_1 <= t, X_2 <= t) (maximum lower than t means that the entire sample is lower than t)
                          = P(X_1 <= t)P(X_2 <= t) (independence)
                          = t²;
        
- Then, what is done is generate two samples based on that distribution, as they have the same one, via inversion method and compare the results with the histogram:

(images\Hist_max_raiz.png)

  This is an illustration of how similar the distributions are.

- At last, we calculate an empyrical CDF based on the simulations and compare it with the analytical one we obtained with the manipulations of the probabilities. The results are shown in the subsequent plot:

(images\Graf_ac_analit_empir.png)

  This shows that, if we try to approximate the analytical (or "real") CDF of the distribution of the variables in question, it will be quite similar to what we obtained analytically, so our simulations worked just as expected.


#  


## Exercise 2:

This code performs a simulation to analyze the behavior of the maximum value in samples drawn from a normal distribution. It consists of two main parts:
i -  Empirical Maximum Calculation:
    Random Number Generation: Uses the Box-Muller transform to generate random numbers from a standard normal distribution.
    Sampling: Creates multiple samples (each with a fixed number of observations) and computes the maximum value from each sample.
    Average of Maximums: Calculates the average of these maximum values to estimate the expected maximum from the distribution.
ii - Theoretical vs. Empirical Comparison:
    Theoretical Calculation: Computes a theoretical estimate of the expected maximum value as a function of the sample size, using a logarithmic expression.
    Empirical Curve Generation: For a range of sample sizes, the code repeats the simulation to build an empirical curve of maximum expectations.
    Visualization: Plots both the theoretical curve and the empirical curve on the same graph to visually compare their behaviors.

Overall, the script compares both curves to check if the theoretical and the empirical curves

The results will change every time the code runs. After all, it is based on random numbers. But below is an example of output:

a = 3.294166288071397

(images\image exercise 2.png)



#


## Exercise 3:

  The question proposed has the purpose of illustrating the result shown in the exercise's statement by the use of an example, where we use the minimum of
three exponentially distributed random variables with specific parameters 1, 2 and 3.

  With that said, all that we had to do was simulate 1000 observations of the minimum's distribution via Inversion Method and compare it with the curve obtained analytically by creating the histogram (with y-axis being the **density**) shown below:

(images\Hist_min_exp_.png)

  By looking at the figure, there's perceptible empyrical evidence that the data simulated by the method is likely to follow the distribution illustrated by the curve. Then, we have a good illustration of the result we got at the start.



#

