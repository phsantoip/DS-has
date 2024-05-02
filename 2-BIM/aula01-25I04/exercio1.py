import os 
os.system("cls")

def preenche_lista(lista:list)->None:
    for i in range(10):
        valor = input("preencha a lista: ")
        lista.append(valor)    
    print(lista)

lista = list()
preenche_lista(lista)
