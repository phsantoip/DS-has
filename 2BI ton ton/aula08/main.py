from subs import *

opcao = 's'
while opcao.upper() == 'S':
    print("1 - Efetuar cálculo de porcentagem.")
    print("2 - Efetuar cálculo de porcentagem através de uma escolha.")
    print("3 - Verificação de nota.")
    print("4 - Exibir o menor valor.")
    i = input("\nDigite a sua opção:")

    match i:
        case '1':
            n = float(input("Digite o valor: "))
            n2 = float(input("Digite a porcentagem: "))

            x = porcentual(n, n2)
            print(f">>> x valerá {x:.1f}")
        case '2':
            n = float(input("Digite o valor: "))
            n2 = float(input("Digite a porcentagem: "))
            tipo = input("Digite o tipo ['a' para acrescimo, 'd' para desconto e 'p' para porcentagem]: ")

            x = porcentual2(n, n2, tipo)
            print(f">>> x valerá {x:.1f}")
        case '3':
            nt = input("Digite sua nota para verificação: ")
            eh_nota(nt)
        case '4':
            n = float(input("Digite um valor: "))
            n2 = float(input("Digite um valor: "))
            n3 = float(input("Digite um valor: "))

            x = menor_3n(n, n2, n3)
            print(f"O menor número é: {x:.1f}")
        case _:
            print("Opção inválida.")

    opcao = input("\n\nRepetir, [s]im ou [n]ão?")
    while opcao.upper() != 'S' and opcao.upper() != 'N':
        opcao = input("\n\nErro, [s]im ou [n]ão?")

'EX1'
"""
n = float(input("Digite o valor: "))
n2 = float(input("Digite a porcentagem: "))

x = porcentual(n, n2)
print(f">>> x valerá {x:.1f}")
"""

'EX2'
"""
n = float(input("Digite o valor: "))
n2 = float(input("Digite a porcentagem: "))
tipo = input("Digite o tipo ['a' para acrescimo, 'd' para desconto e 'p' para porcentagem]: ")

x = porcentual2(n, n2, tipo)
print(f">>> x valerá {x:.1f}")
"""

'EX 3'
"""
nt = input("Digite sua nota para verificação: ")
eh_nota(nt)
"""

'EX 4'
"""
n = float(input("Digite um valor: "))
n2 = float(input("Digite um valor: "))
n3 = float(input("Digite um valor: "))

x = menor_3n(n,n2,n3)
print(f"O menor número é: {x:.1f}")
"""