# SIMULAÇÃO DO LAÇO REPITA
while True:
    n = float(input("Digite um numero: "))
    dobro = float(n + n)
    print(f"{dobro:.1f}")
    if n < 0:
        break
