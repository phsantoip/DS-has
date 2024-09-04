resp = 's'
while resp.upper() == 'S':
    cont = 0
    for i in range(1, 31, 1):
        temperatura = input(f"Digite a temperatura do dia {i}: ")
        if not temperatura.isdigit():
            sol = temperatura.replace(".", "", 1)
            sol2 = temperatura.replace("-", "", 1)
            if sol.isdigit():
                temperatura = float(temperatura)
                if temperatura > 10:
                    cont = cont + 1
            elif sol2.isdigit():
                temperatura = float(temperatura)
                if temperatura > 10:
                    cont = cont + 1
            elif not sol.isdigit():
                sol2 = sol.replace("-", "", 1)
                if sol2.isdigit():
                    temperatura = float(temperatura)
                    if temperatura > 10:
                        cont = cont + 1
                else:
                    print("Digite uma temperatura válida.\n\n")
                    i = 1
                    cont = 0
            else:
                print("Digite uma temperatura válida.\n\n")
                i = 0
                cont = 0
        elif temperatura.isdigit():
            temperatura = float(temperatura)
            if temperatura > 10:
                cont = cont + 1
    print(f"\nDias com temperatura acima de 10ºC: {cont}.")
    resp = input("\nDeseja continuar? (s/n): ")
    while resp.upper() != 'S' and resp.upper() != 'N':
        resp = input("\nErro, [s]im ou [n]ão?")