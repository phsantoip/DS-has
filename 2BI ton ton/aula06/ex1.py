def cubo(n: float) -> float:
    return n * n * n

n = float(input("Digite um número: "))
valor = cubo(n)
print(f"O cubo deste número é: {valor}")