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