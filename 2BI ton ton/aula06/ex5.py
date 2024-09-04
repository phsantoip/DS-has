def fatorial(n: int) -> int:
    n2 = n
    for i in range (1,n,1):
        n2 = n2 - 1
        n = n * n2
    return n

n = int(input("Digite o valor de um numero: "))
f = fatorial(n)
print(f"O valor do fatorial é: {f}")