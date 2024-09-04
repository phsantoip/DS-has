resp = 's'
while resp.upper() == 'S':
    i = 0
    menor = 100000000000000000000000000000000000000000000000000000000
    maior = -10000000000000000000000000000000000000000000000000000000
    while i < 30:
        i = i + 1
        nm = input(f"Digite o {i}º número: ")
        if not nm.isdigit():
            sol = nm.replace(".", "", 1)
            sol2 = nm.replace("-", "", 1)
            if sol.isdigit():
                nm = float(nm)
                if menor > nm:
                    menor = nm
                if maior < nm:
                    maior = nm
            elif sol2.isdigit():
                nm = float(nm)
                if menor > nm:
                    menor = nm
                if maior < nm:
                    maior = nm
            elif not sol.isdigit():
                sol2 = sol.replace("-", "", 1)
                if sol2.isdigit():
                    nm = float(nm)
                    if menor > nm:
                        menor = nm
                    if maior < nm:
                        maior = nm
                else:
                    print("Número Inválido!")
                    i = 0
                    menor = 100000000000000000000000000000000000000000000000000000000
                    maior = -10000000000000000000000000000000000000000000000000000000
        else:
            nm = float(nm)
            if menor > nm:
                menor = nm
            if maior < nm:
                maior = nm

    print(f"\nMenor número: {menor}!\nMaior número: {maior}!")

    resp = input("\nDeseja continuar? (s/n): ")
    while resp.upper() != 'S' and resp.upper() != 'N':
        resp = input("\nErro, [s]im ou [n]ão?")