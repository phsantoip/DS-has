import os
os.system("cls")

valor = int(input("Digite um numro de lados entre (3, 4 e 5): "))

if valor == 3:
    print(f"é um Triangulo")

    tamanho_base = int(input("Tamanho da base(em cm): "))

    tamanho_altura = int(input("Tamanho da altura(em cm): "))

    conta = tamanho_base * tamanho_altura

    print(f"é um triangulo com tamanho da area de {conta} cm")

elif valor == 4:
    print(f"é um Triangulo")

    tamanho_base = int(input("Tamanho da base(em cm): "))

    tamanho_altura = int(input("Tamanho da altura(em cm): "))

    conta = tamanho_base * tamanho_altura

    print(f"é um Quatrado com tamanho da area de {conta} cm")

elif valor == 5:
    print(f"é um Triangulo")

    tamanho_base = int(input("Tamanho da base(em cm): "))

    tamanho_altura = int(input("Tamanho da altura(em cm): "))

    conta = tamanho_base * tamanho_altura

    print(f"é um Pentágono com tamanho da area de {conta} cm")
 
 else:
    print(f"Erro, numero de lados invalido")