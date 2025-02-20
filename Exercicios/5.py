import math
import random

import matplotlib.pyplot as plt


def f(x):
    y = x**4 - 4*x**3 - 2*x**2 - x + 5
    return y


def box_muller(mu=0, sigma=1):
    u1 = random.uniform(0, 1)
    u2 = random.uniform(0, 1)

    z = math.sqrt(-2 * math.log(u1)) * math.cos(2 * math.pi * u2)

    #Para transformar o valor da Z ~ N(0,1) gerado em um valor com média mu, basta transformar:
    x = mu + sigma*z

    return x


def minimizacao_polinomio(x0, n):

    valores_x = []

    for i in range(n):
        if i == 0:
            x_linha = box_muller(mu=x0)
            alfa = math.exp(-f(x_linha))/math.exp(-f(x0))

            # Gerando a uniforme 0,1. Se for <= alfa, então x_t+1 = x', e x_t+1 = x_t caso contrário
            u = random.uniform(0, 1)

            if u <= alfa:
                xt_mais_1 = x_linha
            else:
                xt_mais_1 = x0

        else:
            x_linha = box_muller(mu=valores_x[i-1])
            alfa = math.exp(-f(x_linha))/math.exp(-f(valores_x[i-1]))

            # Gerando a uniforme 0,1. Se for <= alfa, então x_t+1 = x', e x_t+1 = x_t caso contrário
            u = random.uniform(0, 1)

            if u <= alfa: 
                xt_mais_1 = x_linha
            else:
                xt_mais_1 = valores_x[i-1]

        valores_x.append(xt_mais_1)

    return valores_x


valores_x = minimizacao_polinomio(-3, 100000)

valores_y = []

for i in range(len(valores_x)):
    y = f(valores_x[i])
    valores_y.append(y)


valor_minimo = min(valores_y)

indice_minimo = valores_y.index(valor_minimo)

print(f"Valor mínimo: {valor_minimo}")
print(f"Posição do valor mínimo: {indice_minimo}")
print(f"O valor de x correspondente é: {valores_x[indice_minimo]}")


x_minimo = valores_x[indice_minimo]
y_minimo = valores_y[indice_minimo]

# Plotando o gráfico
plt.figure(figsize=(8, 6))
plt.plot(valores_x, valores_y, label='f(x)', linestyle='-', marker='o')  # Curva normal

# Destacando o ponto mínimo
plt.scatter(x_minimo, y_minimo, color='red', s=300, label=f'Mínimo ({x_minimo:.4f}, {y_minimo:.4f})')

# Personalização do gráfico
plt.title('Gráfico de f(x) com Ponto Mínimo Destacado')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)

# Exibir o gráfico
plt.show()
