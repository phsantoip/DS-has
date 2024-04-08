import os
os.system("cls")

def soma_elm(vetor):
    soma = 0 
    for elm in vetor:
        soma += elm
    return soma
vetor = [45, -89, 32, -12, 33]
resultado = soma_elm(vetor)
print("a soma dos elementos do vetor eh:", resultado)
    