def intervalo1(n: float, n2: float) -> None:
    if n > n2:
        aux = n
        n = n2
        n2 = aux

    while n <= n2:
        print(n)
        n = n + 1

def intervalo2(n: float, n2: float, opcao: str) -> None:
    if n > n2:
        aux = n
        n = n2
        n2 = aux

    if opcao == "A":
        intervalo1(n,n2)
    if opcao == 'F':
        while n + 1 < n2:
            n = n + 1
            print(n)

def intervalo3(n: float, n2: float, opcao: str, opcao2: str) -> None:
    if n > n2:
        aux = n
        n = n2
        n2 = aux

    if opcao2 == 'C':
        intervalo2(n,n2,opcao)
    if opcao2 == 'D':
        aux = n
        n = n2
        n2 = aux
        if opcao == 'A':
            while n >= n2:
                print(n)
                n = n - 1
        if opcao == 'F':
            n = n - 1
            while n > n2:
                print(n)
                n = n - 1

def retornar(n: int) -> bool:

    p = 0
    for cont in range(1,n+1,1):
        if n % cont == 0:
            p = p + 1
    if p == 2:
        return True
    else:
        return False

def ordem(n: int, n2: int) -> None:
    if n > n2:
        aux = n
        n = n2
        n2 = aux

    while n <= n2:
        if retornar(n) == True:
            print(n)
        n = n + 1