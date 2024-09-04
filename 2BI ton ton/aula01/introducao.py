# comentários cabulososos
"""
Arthur fofo
Enzo risonho
"""

# variaveis
"""
x = 6
print(x, type(x))
x = "enzinho"
print(x, type(x))
x = 764.2
print(x, type(x))
x = False
print(x, type(x))
"""

#casting
"""
# casting()
conteudo = "0"
print(conteudo, type(conteudo))
conteudo = int(conteudo)
print(conteudo, type(conteudo))
conteudo = float(conteudo)
print(conteudo, type(conteudo))
conteudo = bool(conteudo)
print(conteudo, type(conteudo))
"""

#saida de dados
"""
idade = 48
peso = 2434.2
#exemplo (virgula)
print("Eu tenho", idade, "anos e peso", peso)

#exemplo (mais)
print("Eu tenho" + str(idade) + "anos e peso" + str(peso))
print(type(idade), type(peso))

#utilizando (.format)
print("eu tenho {} anos e peso {}".format(idade,peso))
print("eu tenho {0} anos e peso {1}".format(idade,peso))
print("eu tenho {1} anos e peso {0}".format(idade,peso))
print("eu tenho {0} anos e peso {0}".format(idade,peso))
print("eu tenho {id} anos e peso {p}".format(id = idade,p = peso))
print("eu tenho {id:7d} anos e peso {p:10.3f}".format(id = idade,p = peso))
"""

#octa e hexa
"""
enzo = 25
print("O enzo vale {0} equivalente a:\n{0:o} em octal\n{0:x} em hexadecimal"
    .format(enzo))
diego = -15.4
print(f"Enzo = {enzo:5d}\nDiego = {diego:.2f}")
print("Enzo virgem", end=' Diego Chad')
"""

#operadores aritméticos
'''
valor1 = 17
valor2 = 7
resp = valor1 + valor2
print(resp)
resp = valor1 - valor2
print(resp)
resp = valor1 * valor2
print(resp)
resp = valor1 / valor2
print(resp)
resp = valor1 ** valor2 #exponenciação
print(resp)
resp = valor1 // valor2 #divisão inteira
print(resp)
resp = valor1 % valor2 #módulo
print(resp)
'''

#entrada de dados
'''
v1 = float(input("Digite o valor 1: ")) #input so le string
v2 = float(input("Digite o valor 2: "))

resp = v1 + v2
print(resp);
'''