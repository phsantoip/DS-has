resp = 'S'
while resp.upper() == 'S':
    num = float(input("Numero: "))
    dobro = num + num
    print(f"Dobro = {dobro}")

    resp = input("Continuar, [s]im ou [n]ão?")
    while resp not in ['s','S','n','N']:
        print("ERRO!")
        resp = input("Continuar, [s]im ou [n]ão?")

# v3
'''
resp = 'S'
while resp.upper() == 'S':
    num = float(input("Numero: "))
    dobro = num + num
    print(f"Dobro = {dobro}")

    resp = input("Continuar, [s]im ou [n]ão?")
    while resp.upper() != "S" and resp.upper() != "N":
        print("ERRO!")
        resp = input("Continuar, [s]im ou [n]ão?")
'''

# v2
'''
resp = 's'
while resp in ['s','S']:
    num = float(input("Numero: "))
    dobro = num + num
    print(f"Dobro = {dobro}")

    resp = input("Continuar, [s]im ou [n]ão?")
'''

# v1
'''
resp = 's'
while resp == 's' or resp == 'S':
    num = float(input("Numero: "))
    dobro = num + num
    print(f"Dobro = {dobro}")

    resp = input("Continuar, [s]im ou [n]ão?")
'''