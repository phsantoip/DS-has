import os
os.system('cls')

def calcMedia(v:list) -> int:
    soma = 0
    media = 0
    for cont in v:
        soma += cont
    media = soma / 5
    return media

v = [45, -89, 32, -12, 33]

print(calcMedia(v))