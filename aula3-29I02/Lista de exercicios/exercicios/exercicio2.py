import os
os.system("cls")

ano = int(input("Digite o seu ano de nascimento:"))

idade = 2024 - ano

if idade >= 16:
    print(f"vc tem {idade} anos, então voce pode votar")
else:
     print(f"vc tem {idade} anos, então voce nao pode votar")