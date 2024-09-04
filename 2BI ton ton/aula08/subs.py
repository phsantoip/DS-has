def porcentual(n: float, n2: float) -> float:
    pr = (n * n2) / 100
    return pr

def porcentual2(n: float, n2: float, tipo: str) -> float:
    pr = (n * n2) / 100
    if tipo == 'p':
        r = pr
    elif tipo == 'a':
        r = pr + n
    elif tipo == 'd':
        r = n - pr
    return r

def eh_nota(nt: str) -> None:
    sol = nt.replace(".", "", 1)
    if sol.isdigit():
        nt2 = float(nt)
        if nt2 > 0 and nt2 <= 10:
            print("é nota")
        else:
            print("não é nota")
    else:
        print("não é nota")

def menor_3n(n: float, n2: float, n3: float) -> float:
    if n <= n2 and n <= n3:
        return n
    elif n2 <= n and n2 <= n3:
        return n2
    elif n3 <= n2 and n3 <= n:
        return n3