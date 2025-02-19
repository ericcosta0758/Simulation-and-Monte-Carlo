import numpy as np
import math
import matplotlib.pyplot as plt

n_observações = 1000
n_amostras = 100
Amostra = []
lista_max = []

def box_muller(mu=0, sigma=1):
    u1 = np.random.uniform(0, 1)
    u2 = np.random.uniform(0, 1)
    z = math.sqrt(-2 * math.log(u1)) * math.cos(2 * math.pi * u2)
    x = mu + sigma * z
    return x

for i in range(n_amostras):
    lista_observacoes = []
    for j in range(n_observações):
        x = box_muller()
        lista_observacoes.append(x)
    Amostra.append(lista_observacoes)

for i in Amostra:
    lista_max.append(np.max(i))

Esperanca_max = sum(lista_max) / n_amostras

print(f"a = {Esperanca_max}")

sigma = 1
n_iterado = range(1, 1001)
curva = [math.sqrt(2 * sigma**2 * math.log(n)) for n in n_iterado]

curva_empirica_maxima = []

for n in n_iterado:
    valores_maximos = []
    for _ in range(n_amostras):
        amostra = [box_muller() for _ in range(n)]
        valores_maximos.append(max(amostra))
    curva_empirica_maxima.append(sum(valores_maximos) / n_amostras)

plt.figure(figsize=(10, 6))
plt.plot(n_iterado, curva_empirica_maxima, label="Empírica", color="blue")
plt.plot(n_iterado, curva, label="Teórica", linestyle="dashed", color="red")
plt.xlabel("n")
plt.ylabel("Expectativa Máxima")
plt.title("Comparação entre Expectativa Máxima Empírica e Teórica")
plt.legend()
plt.grid(True)
plt.show()

print("done")