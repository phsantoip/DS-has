from subs import *
resp = "s"
while resp.upper() == "S":
    v = [41, 72, -39, 4, -35]
    v2 = []
    for p in range(0, len(v), 1):
        v2.append(p)
        v2[p] = 0

    print(f"Os vetores são esses:\nv = {v}\nv2 = {v2}")
    linha = "-----------------------------------------------------------------------"
    print(linha)
    print("Nível 1:")
    print("1 - Retornar o primeiro elemento do vetor.")
    print("2 - Exibir somente os numeros negativos do vetor.")
    print("3 - Retornar a soma dos elementos do vetor.")
    print("4 - Retornar a média dos elementos do vetor.")
    print("5 - Exibir os números ímpares do vetor.")
    print("6 - Exibir o primeiro e o último elemento do vetor.")
    print("7 - Exibir os elementos do vetor com índices pares.")
    print("8 - Verificar se há um número em um vetor (TRUE/FALSE).")
    print("9 - Ordenar os elementos do vetor.")
    print(linha)
    print("Nível 2:")
    print("10 - Copiar os elementos do vetor 1 no vetor 2.")
    print("11 - Copiar os elementos do vetor 1 no vetor 2 inverso.")
    print("12 - Ordenar o vetor em ordem crescente.")
    print("13 - Ordenar o vetor em ordem decrescente.")
    print("14 - Ordenar o vetor em uma ordem de sua escolha.")
    print("15 - Posicionar os elementos pares a direita e os ímpares a esquerda.")
    print("16 - Retornar quantos elementos do vetor estão acima da média.")
    print("17 - Retornar o maior elemento do vetor.")
    print("18 - Verificar se há um número em um vetor (TRUE/FALSE).")
    print(linha)

    escolha = input("Escolha sua opção: ")

    match escolha:
        case '1':
            print(retornar_primeiro(v))
        case '2':
            retornar_negativos(v)
        case '3':
            print(somar_elementos(v))
        case '4':
            print(retornar_media(v))
        case '5':
            numeros_impares(v)
        case '6':
            primeiro_ultimo(v)
        case '7':
            indice_par(v)
        case '8':
            print(verificar_existencia(v))
        case '9':
            print(ordenar_elementos(v))
        case '10':
            copia_vetor(v, v2)
        case '11':
            inverte_vetor(v, v2)
        case '12':
            ordena_vetor_crescente(v)
        case '13':
            ordena_vetor_decrescente(v)
        case '14':
            ordena_vetor(v)
        case '15':
            separa_vetor(v)
        case '16':
            print(f"O número de elementos acima da média são: {conta_acima_media(v)}")
        case '17':
            print(f"O maior elemento do vetor é: {maior_elemento(v)}.")
        case '18':
            print(f"Resposta: {busca_vetor(v)}.")
        case _:
            print("Escolha Inválida")

    resp = input("\nDeseja reiniciar o programa? (S/N): ")
    while resp.upper() != "S" and resp.upper() != "N":
        resp = input("Erro!Digite [S]im ou [N]ão: ")