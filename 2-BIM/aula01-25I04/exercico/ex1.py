import os 
os.system("cls")

"""
1. Fazer um procedimento chamado ‘preenche_lista(l)’ que preencha uma lista passada por parâmetro.
	preenche_lista(lista)
"""


def prenche_lista(lista:list) -> None:

    while True:
        index = input("preencha a lista: ")
        lista.append(index)
        if index == '.':
            break

    lista.remove('.')
    print(lista)

lista = []

"""
2. Fazer um procedimento chamado ‘exibe_lista(l)’ que exiba os elementos da lista passada por parâmetro..
	exibe_lista(lista)
"""

def exibe_lista(lista):
    print(prenche_lista(lista))


exibe_lista(lista)


              