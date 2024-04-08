# dadas 3 notas, tirar a menor e calcular a media dos outro 
def menor3n(n1, n2, n3):
    menor = n1
    if n2 < menor:
        menor = n2
    if n3 < menor:
        menor = n3
    return menor

def media2maiores(n1: float, n2: float, n3: float) ->float:
    return ( n1 + n2 + n3 - menor3n(n1, n2, n3)) / 2

# ------------- Programa principal
import os
os.system("cls")
nota1 = 5
nota2 = 1
nota3 = 2
print(f"Media: {media2maiores(nota1, nota2, nota3)}")
