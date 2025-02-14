import math
import numpy as np
def box_muller(mu=0, sigma=1):
    u1 = random.uniform(0,1)
    u2 = random.uniform(0,1)

    z = math.sqrt(-2 * math.log(u1)) * math.cos(2 * math.pi * u2)

    #Para transformar o valor da Z ~ N(0,1) gerado em um valor com média mu, basta transformar:
    x = mu + sigma*z

    return x