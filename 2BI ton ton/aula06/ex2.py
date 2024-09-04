def potência(base: float, expoente: float) -> float:
    base1 = base
    for i in range (1,expoente,1):
        base = base * base1
    return base

base = int(input("Digite o valor da base: "))
expoente = int(input("Digite o valor do expoente: "))
valor = potência (base, expoente)
print(f"O valor da potência é: {valor}")