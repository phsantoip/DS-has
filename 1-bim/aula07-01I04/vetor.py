import os 
os.system ("cls")
# ------------ SUBALGORITMOS
def exibe_vetor(v:list) -> None:
 for i in range (0, 5, 1):
   print (f"Posição (1): (vet(i))")

# 1. Fazer uma função que retorne o primeiro elemento do vetor.'
# vetor.
   
def exibe_primeiro_elemento(vet: list) -> int:
  return vet [0]

# ---------- PROGRAMA PRINCIPAL 
#     0  1  2  3  4
# Iniciando vetor 

V = [45, 34, 23, 12, 67]
exibe_vetor(V)
print(exibe_primeiro_elemento(V))

''' Dado o vetor por parametro e a posição a ser exibida, faça uma função chamada 'exibe_posição' que exiba o elemento correspondente.
 Considerar que o vetor tenha 5 elementos, caso a posição informada seja fora deste intervalo, exibir a primeira posição
'''





