"""
2. Fazer um procedimento chamado ‘exibe_lista(l)’ que exiba os elementos da lista passada por parâmetro..
	exibe_lista(lista)
"""
import os
os.system("cls")

def exibe_lista(lista):
    lista.append(26)
    lista.append(30)
    lista.append(40)
    print(lista)

lista = list()
exibe_lista(lista)

