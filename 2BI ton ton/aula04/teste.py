#Somar numero até que seja digitado zero
soma = 0
n = 1

while n != 0: #Laço pós-condicional (executa enquanto for verdade)
    n = int(input("Digite um numero: "))
    if n < 0:
        print("Digite um número positivo!")
        continue #Força o retorno ao inicio do laço
    if n >= 10:
        break #Força a saída do laço
    soma = soma + n
else: #Executa caso tudo transcorra normalmente no laço
    print("Laço executado sem interrupção.")
print(soma)
