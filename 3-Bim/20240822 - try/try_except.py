"""
try:
    comandos a serem executados
except:
    codigos caso haja erro
else:
    codigos caso não haja erro
finally:
    codigos com erro ou não
"""


import os
os.system("cls")

try: 
    valor1 = float(input("Valor 1:"))
    valor2 = float(input("Valor 2:"))
    divisao = valor1 / valor2
    print(f"Divisão = {divisao}")
except ValueError:
    print("Digite um valor numérico!")
except ZeroDivisionError as erroZero:
    print(f"Erro! {erroZero}")
except:
    print("Mano, chama o administrador que moiô!")
else:
    print("Divisão efetuada com sucesso!")
finally:
    print("Saindo do sistema")