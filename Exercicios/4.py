import random

# definir elementos
portas = [1, 2, 3]
premios = ["carro", "cabra", "cabra"]

# função para embaralhar a lista


def embaralhar(lista):

    numeros_aleatorios = [random.uniform(0,1) for i in range(len(lista))]

    pares = list(zip(numeros_aleatorios, lista))

    pares.sort(key=lambda x: x[0])

    lista_embaralhada = [j[1] for j in pares]

    return lista_embaralhada


def monty_hall(portas, premios, manter=True, n=1000):
    resultados = []

    for _ in range(n):
        # Embaralhar as portas e os prêmios
        portas = embaralhar(portas)
        premios = embaralhar(premios)

        # Combinar portas e prêmios
        combinado = list(zip(portas, premios))

        # Escolha aleatória do participante usando uniform
        escolha_unif = random.uniform(0, 1)
        escolha_index = int(escolha_unif * 3)  # Convertendo para 0, 1 ou 2
        escolha_participante = combinado[escolha_index]

        # Identificar as portas não escolhidas
        portas_restantes = [i for i in range(3) if i != escolha_index]

        # O apresentador revela uma cabra de uma das portas restantes usando uniform
        portas_com_cabra = [i for i in portas_restantes if combinado[i][1] == "cabra"]
        if len(portas_com_cabra) > 1:
            escolha_revelada_unif = random.uniform(0, 1)
            index_revelada = int(escolha_revelada_unif * len(portas_com_cabra))
            porta_revelada = portas_com_cabra[index_revelada]
        else:
            porta_revelada = portas_com_cabra[0]

        # Atualizar as portas restantes após a revelação
        portas_restantes.remove(porta_revelada)

        # Decisão do participante: manter ou trocar
        if manter:
            escolha_final = escolha_participante
        else:
            # Há apenas uma porta restante para trocar
            nova_porta_index = portas_restantes[0]
            escolha_final = combinado[nova_porta_index]

        # Verificar se o prêmio é o carro
        if escolha_final[1] == "carro":
            resultados.append(1)
        else:
            resultados.append(0)

    return resultados


# Simulando para 10000 casos mantendo e não mantendo a decisão inicial
mantendo = monty_hall(portas, premios, manter=True, n=10000)
proporcao_mantendo = sum(mantendo)/len(mantendo)
print(f"A proporção de vitórias no caso em que o participante mantém a escolha é de {proporcao_mantendo}.")

nao_mantendo = monty_hall(portas, premios, manter=False, n=10000)
proporcao_nao_mantendo = sum(nao_mantendo)/len(nao_mantendo)
print(f"A proporção de vitórias no caso em que o participante não mantém a escolha é de {proporcao_nao_mantendo}.")