# VERIFICAR SE UM DADO É UM NÚMERO
# Leitura do texto correspondete ao numero
num = input("Numero: ")
# Verifico se o texto digitado corresponde a um int
if num.isdigit(): # isdigit() verifica se é um numero int
    # executou o cálculo
    num = float(num)
    dobro = num + num
    print(f"Dobro = {dobro}")
else:
    # não é um texto int
    # tira um ponto pra verificar se é float
    cobaia = num.replace(".","",1)
    # Verifico se é um numero
    if cobaia.isdigit():
        # executa a operacao
        num = float(num)
        dobro = num + num
        print(f"Dobro = {dobro}")
    else:
        # informa que não é um valor float
        print("não é um numero")