resp = 's'
while resp.upper() == 'S':
    numero = input("Digite um número decimal para que ele seja convetido para binário: ")
    if numero.isdigit():
        numero2 = int(numero)
        numero2 = bin(numero2)
        sol = numero2.replace("0b","",1)
        print(f"\nO número em binário é: {sol}.")

        resp = input("\n\nContinuar, [s]im ou [n]ão?")
        while resp.upper() != 'S' and resp.upper() != 'N':
            resp = input("\n\nErro, [s]im ou [n]ão?")
    else:
        print("Digite um número decimal!")
        resp = input("\n\nContinuar, [s]im ou [n]ão?")
        while resp.upper() != 'S' and resp.upper() != 'N':
            resp = input("\n\nErro, [s]im ou [n]ão?")