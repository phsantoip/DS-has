import os
os.system("cls")
Altura = float(input("Digite sua altura: "))

print("""
informe seu sexo:
          
1 - Masculino
2 - Feminino
    """)

opcao = int(input("Escolha: "))
match opcao:
    case 1:
       homens = (72.7 * Altura) - 58
       print(f"Seu peso ideal é: {homens}")
    case 2:
       mulheres = (62.1 * Altura) - 44.7
       print(f"Seu peso ideal é: {mulheres}")