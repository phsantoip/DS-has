def preencher(i:int) -> list:
    vet = []
    n = 1
    for p in range(0, i, 1):
        vet.append(p)
        vet[p] = int(input(f"Digite o valor do {n}º índice: "))
        n += 1
    return vet