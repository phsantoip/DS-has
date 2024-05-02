# Formatações
texto = "ph e vh"
valor = 23
salario = 1234.56
filhos = True
print("Boa tarde" + texto)
print("Boa tarde", texto)
print("Valor =", valor)
print("Nome {} {}".format(texto, valor))
print("Nome {1} {0}".format(texto, valor))
print("Nome {0} - {1} - {2} - {3}".format(texto, valor, salario, filhos))
print("Salario: {0} ".format(salario))
print("Salario: {0:.3f} ".format(salario))
print("Salario: {0:.4f} ".format(salario))
print("Salario: {0:.2f} ".format(salario))
print("Salario: {0:.10.2f} ".format(salario))
print("Salario: {0:.8.2f} ".format(salario))
print("Valor: {0:5} ".format(valor))
print("Valor: {0:05} ".format(valor)) 

