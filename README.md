# Simulation-and-Monte-Carlo

## Introduction

  This project has been developed with the intent to analyze various problems, which solutions should involve various methods that were exposed and discussed in the classes of the discipline throughout the semester. With that in mind, most of the work was done in the most pedagogically pertinent way, avoiding the use of many libraries available in Python that would make all the methodology present in the solutions entirely implicit.
  
## Methodology
  With all of that in mind, the main methods that were used in this project are quickly described in the following section.
  
  - The *Inversion Method* consists in using the analytical or recursive CDF of the distribution (which follows the Uniform[0,1] distribution) of the variable (that must have one of these known) to, via inversion of the said cumulative by the use of the expression "u = F(x)", obtain the expression of x and simulate said variable.
  
  - The *Box-Muller Method* is used to simulate normally distributed variables using the knowledge that, being X and Y both normally distributed with mean 0 and variance 1,
    ***IMAGEM DA FÓRMULA MATEMÁTICA FEITA NO LATEX, COLOCO DEPOIS***


    Where R follows the Rayleigh(1) distribution and θ follows an Uniform[0,2π] distribution. This method uses the same idea used to prove that the CDF of the Normal(0, 1) distribution, when applied on infinity, integrates to 1.

    
  
