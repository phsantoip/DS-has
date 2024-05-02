import os 
os.system("cls")

def listaPonto(lista:list) -> None:

    while True:
        index = input()
        lista.append(index)
        if index == '.':
            break

    lista.remove('.')
    print(lista)

lista = []

print(listaPonto(lista))

"""
1. Tranforme esta rotina em um procedimento.
2. Fazer um programa que pegue o indice e o elemento e insira-o na lista. 
"""

              