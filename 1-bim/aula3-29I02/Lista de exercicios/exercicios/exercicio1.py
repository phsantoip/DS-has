import os
os.system("cls")

n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro: "))

if n1 < n2:
    print(f"o numero maior é {n2}")
else:
    print(f"o numero maior é {n1}")