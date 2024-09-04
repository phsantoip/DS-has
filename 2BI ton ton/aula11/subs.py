def preenche_lista(l:list) -> None:
    n = int(input("Digite o número de dados que deseja preencher na lista:"))
    for i in range(0,n,1):
        x = input(f"Índice {i}: ")
        l.append(x)

def exibe_lista(l:list) -> None:
    print("Elementos da lista:")
    for i in range(0, len(l), 1):
        print(f"Índice {i}: {l[i]}")
    print(l)

def conta_elementos(l:list) -> int:
    return len(l)

def retorna_indice(elemento:str, l:list) -> float:
    x = 0
    for i in range(0, len(l), 1):
        if elemento == l[i]:
            x +=1
    if x > 0:
        return l.index(elemento)
    else:
        return -1

def busca(elemento:str, l:list) -> float:
    x = l.count(elemento)
    return x

def conta_inteiro(l:list) -> int:
    x = 0
    for i in range(0, len(l), 1):
        l[i] = str(l[i])
        if l[i].isdigit():
            l[i] = int(l[i])
            x += 1
    return x