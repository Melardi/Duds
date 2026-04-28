import random

def rolar_dados(n):
    lista_final = []
    lista =[0]*n
    for i in range(len(lista)):
        x = random.randint(1, 6)
        lista_final.append(x)
    return lista_final 






def guardar_dado(lista_dados_rolados, lista_dados_guardados, indice_dado_para_guardar):
    
    valor_dado_para_guardar = lista_dados_rolados[indice_dado_para_guardar]

    nova_lista_dados_rolados = []
    for i in range(len(lista_dados_rolados)):
        if i != indice_dado_para_guardar:
            nova_lista_dados_rolados.append(lista_dados_rolados[i])
    
    lista_dados_guardados.append(valor_dado_para_guardar)

    lista_resultado = [nova_lista_dados_rolados, lista_dados_guardados]

    return lista_resultado






def remover_dado(lista_dados_rolados, lista_dados_guardados, indice_dado_para_remover):

    valor_dado_para_remover = lista_dados_guardados[indice_dado_para_remover]

    nova_lista_dados_guardados = []
    for i in range(len(lista_dados_guardados)):
        if i != indice_dado_para_remover:
            nova_lista_dados_guardados.append(lista_dados_guardados[i])
    
    lista_dados_rolados.append(valor_dado_para_remover)

    lista_resultado = [lista_dados_rolados, nova_lista_dados_guardados]

    return lista_resultado






def calcula_pontos_regra_simples(lista_dados_rodados):
    pontuação = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

    for i in range(len(lista_dados_rodados)):
        face = lista_dados_rodados[i]
        pontuação[face] += face
    
    return pontuação






def calcula_pontos_soma(lista_dados_rolados):
    soma_das_faces = 0

    for i in range(len(lista_dados_rolados)):
        soma_das_faces += lista_dados_rolados[i]

    return soma_das_faces






def calcula_pontos_sequencia_baixa(lista_dados_rolados):
    sequencias = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]

    for seq in sequencias:
        contador = 0
        for valor in seq:
            if valor in lista_dados_rolados:
                contador += 1
        if contador == 4:
            return 15

    return 0






def calcula_pontos_sequencia_alta(lista_dados_rolados):
    sequencias = [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6]]

    for seq in sequencias:
        contador = 0
        for valor in seq:
            if valor in lista_dados_rolados:
                contador += 1
        if contador == 5:
            return 30
    
    return 0
