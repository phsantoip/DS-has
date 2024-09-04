resp = 's'
while resp.upper() == 'S':
    n = input("Digite um numero positivo inteiro: ")
    if not n.isdigit():
        print("\n\nDigite um numero positivo inteiro!")
        resp = input("\n\nContinuar, [s]im ou [n]ão?")
        while resp.upper() != 'S' and resp.upper() != 'N':
            resp = input("\n\nErro, [s]im ou [n]ão?")