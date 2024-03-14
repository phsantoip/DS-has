import os 
os.system('cls')
 
print("""
Exercicio 1
Exercicio 2
Exercicio 3
Exercicio 4
Exercicio 5
Exercicio 6
Exercicio 7
Exercicio 8
Exercicio 9
Exercicio 10
Exercicio 11
""")

menu = int(input("Digite o Exercicio que deseja realizar: "))

match menu:
    case 1:

        n1 = int(input("Digite um numero: "))
        n2 = int(input("Digite outro: "))

        if n1 < n2:
            print(f"o numero maior é {n2}")
        else:
             print(f"o numero maior é {n1}")

    case 2:

        ano = int(input("Digite o seu ano de nascimento:"))

        idade = 2024 - ano

        if idade >= 16:
            print(f"vc tem {idade} anos, então voce pode votar")
        else:
            print(f"vc tem {idade} anos, então voce nao pode votar")

        case 3:   
      