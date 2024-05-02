# variaveis em Pyton não são tipadas 
x = 10
print(x, type(x))
x = 10.5
print(x, type(x))
x = "2BI"
print(x, type(x))
x = True
print(x, type(x))
"""
int - inteiro
float - real
str - string | Texto
bool - logico
""" 
# Casting - Ato de mudar o tipo de variavel via codigo

'''
int ()
float()
str()
bool()
'''
x = 25
x= bool(x)
print(x, type(x))
# Entrada de dados - input() ~ scanf()
# O input sempre lê dados str
valor1 = int(input("Digite o 1.o numero:"))
valor2 = int(input("Digite o 2.o numero:"))
resposta = valor1 + valor2 
print("Resposta:", resposta)

# Formatações
texto = "ph"
valor = 23
salario = 1234.56
filhos = True
print("Boa tarde" + texto)
print("Boa tarde", texto)
print("Valor =", valor)
print("Nome {} {}".format(texto, valor))