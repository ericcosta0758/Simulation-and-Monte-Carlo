### Questão 3

import numpy as np
import matplotlib.pyplot as plt
## Nesse caso, estamos simulando o mínimo entre 3 exponenciais específicas, mas
#teria problema fazer geral e aplicar? Acho que tudo bem, desde que a aplicação
#no final seja específica, né?

def SimulaMinExp(taxas, tamAmostra=1):
    amostra = [ ]

    for i in range(tamAmostra):
        unif = np.random.rand()
        
        elem = -np.log(1-unif)/np.sum(taxas)
        amostra.append(elem)

    return(amostra)

testeSim = SimulaMinExp([1, 2, 3])

## Isso conclui o código pedido no item 1.

sim_Min = SimulaMinExp([1,2,3], 1000)

#

x = [i/1200 for i in range(1200)]

obsTeo = [(1 + 2 + 3)*np.e**(-(1+2+3)*i) for i in x]

plt.hist(sim_Min, color='darkblue', bins=40, edgecolor='black', density=True, label='Dist.Simulada Mín.')
plt.plot(x, obsTeo, color='red', label='Dist.Analítica Mín.')


plt.show()
