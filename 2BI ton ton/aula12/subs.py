def preenche_lista(l: list) -> None:
    i = "s"
    ind = 0
    while i != ".":
        l.append(ind)
        l[ind] = input(f"Digite o elemento do indíce {ind}: ")
        if l[ind] == ".":
            l.pop(ind)
            i = "."
        ind += 1

def preenche_numerico(l:list, ln:list)  -> None:
    for i in range(len(l)):
        if l[i].isdigit():
            ln.append(int(l[i]))

def preenche_nao_numerico(l:list, lnn:list)  -> None:
    for i in range(len(l)):
        if l[i].isdigit() == False:
            lnn.append(l[i])

def conta_numericos(l:list) -> int:
    y = 0
    for i in range(len(l)):
        if l[i].isdigit():
            y += 1
    return y

def conta_nao_numericos(l:list) -> int:
    y = 0
    for i in range(len(l)):
        if l[i].isdigit() == False:
            y += 1
    return y

def conta_numericos_reais(l:list) -> int:
    y = 0
    for i in range(len(l)):
        sol = l[i].replace(".", "", 1)
        if l[i].isdigit():
            y += 1
        elif sol.isdigit():
            y +=1
    return y