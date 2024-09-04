def checar(n: float, n2: float, n3: float) -> None:
    if n2 < n:
        aux = n
        n = n2
        n2 = aux

    while n < n2:
        n = n + 1
        if n % n3 == 0:
            print (n)

def delta(a: float, b:float, c:float) -> float:
    delta = (b * b) - (4 * a * c)
    return delta