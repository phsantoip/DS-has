resp = 's'
while resp.upper() == 'S':
    qt = input("Digite a quantidade de número que deseja somar: ")
    soma = 0
    if qt.isdigit():
        cont = int(qt)
        for i in range(1,cont+1,1):
            nm = input(f"Digite o {i}º número: ")
            sol = nm.replace(".", "", 1)
            sol = sol.replace("-", "", 1)

            while not sol.isdigit():
                print("Número Inválido!")
                nm = input(f"Digite o {i}º número: ")
                sol = nm.replace(".","", 1)
                sol = sol.replace("-", "", 1)
            soma = soma + float(nm)
        print(f"\nResultado da soma: {soma:2.2f}!")

        resp = input("\n\nContinuar, [s]im ou [n]ão?")
        while resp.upper() != 'S' and resp.upper() != 'N':
            resp = input("\n\nErro, [s]im ou [n]ão?")
    else:
        print("ERRO! Digite um número válido.")
        resp = input("\n\nContinuar, [s]im ou [n]ão?")
        while resp.upper() != 'S' and resp.upper() != 'N':
            resp = input("\n\nErro, [s]im ou [n]ão?")