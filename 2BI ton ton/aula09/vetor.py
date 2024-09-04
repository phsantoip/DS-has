# ----- DEFINIÇÃO DO VETOR COM 5 POSIÇÕES
#    0    1   2  3   4    5<= índices
v = [34, 54, 67, 89, 12, 77] # <= elementos

# ----- DEFINIÇÃO DOS SUBALGORITMOS
# PROCEDIMENTOS
def exibe_vetor(vet: list) -> None:
    for i in range(0, len(vet), 1):
        print(f"{i} = {vet[i]}")

# FUNÇÕES
def ultimo_elemento(vet: list) -> int:
    return vet[len(vet) - 1]

# ----- PRINCIPAL

exibe_vetor(v)
print(ultimo_elemento(v))

# ----- Exemplos
'''
print(v[3])
v[0] = int(input())
print(v[0])
print("tem ", len(v)) # Conta a quantidade de elementos do vetor
'''

"""
EXERCÍCIOS:
1. Fazer uma Função que retorne o primeiro elemento do vetor
2. Fazer um procedimento que exiba somente os numeros negativos contidos no vetor
3. Fazer uma função que retorne a soma dos elementos do vetor
4. Fazer uma função que retorne a media dos elementos do vetos
5. Fazer um procedimento que exiba na tela os numeros ímpares contidos no vetor
6. fazer um procedimento que exiba na tela o primeiro e o ultimo elemento do vetor
7. Fazer um procedimento que exiba os elementos cujos índices sejam pares
8. Fazer uma função que retorne True caso um valor passado por parâmetro exista no vetor, senão False
9. Fazer uma função que ordene os elementos do vetor.
"""

