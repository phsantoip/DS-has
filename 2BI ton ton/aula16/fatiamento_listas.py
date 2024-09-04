def posicoes(frase: str, elemento: str) -> list:
    list = []
    t = 1
    c = 0
    while (t == 1):
        i = frase.find(elemento, c)
        c=i+1
        if (i != -1):
            list.append(i)
        else:
            t = 0
    return list

frase = "veremos agora o método de manipulação de strings"
elemento = input("Digite um elemento a ser passado por parâmetro: ")
print(posicoes(frase, elemento))
