from subs import *

l = []
print("A lista está vazia.")
print("\n1 - Preencher a lista.")
preenche_lista(l)
print("\n2 - Exibir a lista.")
exibe_lista(l)
print("\n3 - Contar o número de elementos da lista.")
print(f"A lista possui {conta_elementos(l)} elementos.")
print("\n4 - Retornar o índice de um elemento passado por parâmetro. (caso não exista, retorna -1)")
n = input("Digite o elemento a ser passado por parâmetro: ")
print(f"Índice: {retorna_indice(n,l)}.")
print("\n5 - Retornar a quantidade de um elemento passado por parâmetro em uma lista.")
n2 = input("Digite o elemento a ser passado por parâmetro: ")
print(f"Quantidade: {busca(n2,l)}.")
print("\n6 - Retornar a quantidade de números inteiros em uma lista.")
print(f"Quantidade de número inteiros: {conta_inteiro(l)}.")


