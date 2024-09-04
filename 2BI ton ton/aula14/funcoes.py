#1
def preenche_lista(l: list) -> None:
    while True:
        dado = input("Digite um dado: ")
        if dado != ".":
            l.append(dado)
        else:
            break

#2
def exibe_lista(l: list) -> None:
    for ind, elem in enumerate(l):
        print(f"Posicao {ind} = {elem}")
    print("\nLista = ",l)

#3
def conta_elementos(l:list) -> int:
    qtd = 0
    for elem in l:
        qtd = qtd + 1
    return qtd

#4
def retorna_indice(elemento: str, l:list) -> int:
    resp = -1
    resp2 = -1
    for ind, elem in enumerate(l):
        if elemento == str(elem):
            resp = ind
            break
    for ind, elem in enumerate(l):
        if elemento == str(elem):
            resp2 = ind
    if resp2 == resp:
        return resp
    else:
        return resp, resp2

#5
def busca(l:list, elemento:str) -> int:
    qtd = 0
    for elem in l:
        if elemento == elem:
            qtd += 1
    return qtd

#6
def conta_inteiro(l:list) -> int:
    qtd = 0
    for elem in l:
        sol = elem.replace("-","",1)
        if elem.isdigit():
            qtd = qtd + 1
        elif sol.isdigit():
            qtd = qtd + 1
    return qtd

#7
def conta_string(l:list) -> int:
    qtd = 0
    for elem in l:
        if elem.isdigit() == False:
            sol = elem.replace(".","",1)
            sol2 = elem.replace("-","",1)
            if sol.isdigit() == False and sol2.isdigit() == False:
                sol3 = sol.replace("-","",1)
                if sol3.isdigit() == False:
                    if elem != "True" and elem != "False":
                        qtd = qtd + 1
    return qtd

#8
def conta_boolean(l:list) -> int:
    qtd = 0
    for elem in l:
        if elem == "True" or elem == "False":
            qtd += 1
    return qtd

#9
def conta_float(l:list) -> int:
    qtd = 0
    for elem in l:
        if elem.isdigit() == False:
            sol = elem.replace(".","",1)
            sol2 = elem.replace("-","",1)
            sol3 = sol.replace("-","",1)
            if sol.isdigit():
                qtd = qtd + 1
            elif sol2.isdigit() == False and sol3.isdigit():
                qtd = qtd + 1
    return qtd

#10
def copia_int(l:list, l2: list) -> None:
    for elem in l:
        sol = elem.replace("-","",1)
        if elem.isdigit():
            l2.append(elem)
        elif sol.isdigit():
            l2.append(elem)