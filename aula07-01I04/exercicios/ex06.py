import os
os.system('cls')

def exibeExtremos():
    for cont in v:
        if cont == v[0] or cont == v[-1]:
            print(cont, '', end='')
        
v = [45, -89, 32, -12, 33]

exibeExtremos()