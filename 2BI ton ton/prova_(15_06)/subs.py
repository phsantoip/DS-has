def preenche_lista(lista:list) -> None:
    for i in range(0,5,1):
        lista.append(i)
        lista[i] = input(f"Digite o valor do índice {i}: ")
    print(f"Lista: {lista}")

def preenche_nao_digito(lista:list, lista_nao_digito:list) -> None:
    n = 0
    for i in range(0,len(lista),1):
        if lista[i].isdigit() == False:
            lista_nao_digito.append(n)
            lista_nao_digito[n] = lista[i]
            n += 1
    print(f"Lista sem dígitos: {lista_nao_digito}")