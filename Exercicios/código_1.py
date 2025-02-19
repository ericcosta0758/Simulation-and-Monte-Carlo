### Questão 1

import numpy as np
import scipy.stats as stats #Para calcular a empírica. Era para ser de outra forma?
# Acabei de perceber que dá pra fazer na mão calculando os quantis por conta própria. É isso?
import matplotlib.pyplot as plt
## Pulemos, inicialmente, a parte demonstrativa (até passar para o arquivo definitivo),
#mas essa se trata somente de substituições em meio à FDC da variável Z.

## Podemos simular as distribuições de Y e Z pelo método da inversão, pelo qual 
#podemos obter que t = sqrt(u), u sendo uma observação de uma uniforme [0,1]. As-
#sim,

def simula_Y_e_Z(tamAmostra):
    amostra = [ ]
    
    for i in range(tamAmostra):
        unif = np.random.rand()

        elem = np.sqrt(unif)
        amostra.append(elem)

    return(amostra)

sim_Y = simula_Y_e_Z(1000)
sim_Z = simula_Y_e_Z(1000)

## Histograma comparando as distribuições:

plt.figure()
plt.hist(sim_Y, color='blue', edgecolor='black', label='Dist.Máximo')
plt.hist(sim_Z, color='black', edgecolor='black', alpha=0.6, label='Dist.Raíz')
plt.title('Histograma das observações obtidas das simulações de Y (máximo) e Z (raíz).')
plt.xlabel('Valores observados')
plt.ylabel('Frequência absoluta')
plt.legend()

#

## Gráfico comparando as F. Distrib. Acumuladas empírica e analítica:

acEmpírica = stats.ecdf(sim_Y).cdf ## Acumulada Empírica pelo SciPy
acAnalítica = np.square(sorted(sim_Y))

plt.figure()
plt.plot(sorted(sim_Y), acAnalítica, color='darkgreen', label='Ac.Analítica')
plt.plot(acEmpírica.quantiles, acEmpírica.probabilities, color='red', label='Ac.Empírica')
plt.xlabel('Valores (ac. analítica) ou quantis (ac. empírica)')
plt.ylabel('Densidade Acumulada')
plt.legend()

plt.show 
