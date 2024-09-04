from subs import *

lista = []
lista_numerico = []
lista_nao_numerico = []
resp = "s"
while resp.upper() == "S":
    print(f"\nEssa é a lista atual = {lista}")
    linha = "------------------------------------------------------------------------------------------------"
    print("\nMenu de operações envolvendo listas!")
    print(linha)
    print("1 - Preencher a lista até que um ""."" seja digitado!")
    print(linha)
    print("2 - Jogar em uma segunda lista somente os elemento numéricos da lista original!")
    print(linha)
    print("3 - Jogar em uma segunda lista somente os elemento não numéricos da lista original!")
    print(linha)
    print("4 - Retornar quantos elementos numéricos existem na lista original!")
    print(linha)
    print("5 - Retornar quantos elementos não numéricos existem na lista original!")
    print(linha)
    print("6 - Retornar quantos elementos numéricos existem na lista original! (Incluindo os números reais)")

    opcao = input("\n\nDigite sua escolha: ")

    match(opcao):
        case "1":
            preenche_lista(lista)
            print(f"Lista = {lista}")
        case "2":
            preenche_numerico(lista, lista_numerico)
            print(f"Lista com elementos numéricos = {lista_numerico}")
        case "3":
            preenche_nao_numerico(lista, lista_nao_numerico)
            print(f"Lista com elementos não numéricos = {lista_nao_numerico}")
        case "4":
            print(f"Quantidade de elementos numéricos na lista = {conta_numericos(lista)}")
        case "5":
            print(f"Quantidade de elementos não numéricos na lista = {conta_nao_numericos(lista)}")
        case "6":
            print(f"Quantidade de elementos numéricos na lista (incluindo os números reais) = {conta_numericos_reais(lista)}")
        case _:
            print("Escolha Inválida!")

    resp = input("\nDeseja reiniciar o programa? (s/n): ")
    while resp.upper() != 'S' and resp.upper() != 'N':
        resp = input("\nErro, [s]im ou [n]ão?")