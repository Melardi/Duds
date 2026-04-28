import random

def rolar_dados(n):
    lista_final = []
    lista =[0]*n
    for i in range(len(lista)):
        x = random.randint(1, 6)
        lista_final.append(x)
    return lista_final 