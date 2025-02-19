# Simulation-and-Monte-Carlo






Exercise 2:

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
And the image exercise 2.png