from funcoes import *

#lista = ['11','-15','20.50','20.50','True','texto','exercicio','54', '54', '-9.2']
lista = []
lista2 = []
linha="---------------------------------------------------------------------"
i = 's'
while i.upper() == 'S':
    print("\n\n", linha)
    print("1 - Preencher a lista até que seja digitado um ponto final.\n")
    print("2 - Exibir a lista.\n")
    print("3 - Contar quantos elementos existem na lista.\n")
    print("4 - Retornar o índice de um elemento dado pelo usuário.\n")
    print("5 - Retornar a quantidade de um elemento passado pelo usuário.\n")
    print("6 - Contar quantos números inteiros existem na lista.\n")
    print("7 - Contar quantos elementos strings existem na lista.\n")
    print("8 - Contar quantos elementos lógicos existem na lista. (True/False)\n")
    print("9 - Contar quantos elementos do tipo float existem na lista.\n")
    print("10 - Jogar em uma segunda lista somente os números inteiros da lista original!")
    print(linha)
    print(f"Lista atual: {lista}")
    print(linha)

    decisao = input("Digite sua escolha: ")
    print("\n")
    match(decisao):
        case '1':
            preenche_lista(lista)
            print("\nLista = ",lista)
        case '2':
            exibe_lista(lista)
        case '3':
            print("A quantidade de elementos na lista é:", conta_elementos(lista))
        case '4':
            print("Aviso: caso o elemento não se encontre na lista, o índice será representado por -1.\n")
            print("O índice do elemento dado é:", retorna_indice(input("Digite o elemento a ser passado por parâmetro: "), lista))
        case '5':
            print("A quantidade de vezes que esse elemento está na lista é:", busca(lista, input("Digite o elemento a ser passado por parâmetro: ")))
        case '6':
            print("A quantidade de números inteiros nessa lista é: ",conta_inteiro(lista))
        case '7':
            print("A quantidade de elementos do tipo string nessa lista é: ",conta_string(lista))
        case '8':
            print("A quantidade de elementos do tipo boolean nessa lista é: ",conta_boolean(lista))
        case '9':
            print("A quantidade de elementos do tipo float nessa lista é: ",conta_float(lista))
        case '10':
            copia_int(lista, lista2)
            print(f"Lista 1: {lista}\nLista 2: {lista2}")
        case _:
            print("Escolha Inválida!")
        
    i = input("\nDeseja reiniciar o programa? (s/n): ")
    while i.upper() != 'S' and i.upper() != 'N':
        i = input("\nErro, [s]im ou [n]ão?")