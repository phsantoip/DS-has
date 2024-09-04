# Parâmetros Default

def saudacao(msg: str = "Bom dia", nome: str = "Usuário") -> None:
    print(f"{msg} {nome}!")


saudacao("Boa Tarde", "Edson")
saudacao()
saudacao("Edson")
saudacao(nome = "Maria")

# EXERCÍCIOS
"""
1 - Dado o nome do paciente e a hora da colsulta, exibir mensagem:
"XXXX sua colsulta é as 99 horas"
Os padrões dos parâmetros será "Paciente" e horario "8"
2 - A partir de 3 numeros, retornar o de maior valor, se nao forem passados parametro, considerar os valores 1, 2 e 3 respectivamente  
"""


# Exercício 1

def consulta(pac: str = "Paciente", hora: str = "08:00"):
    print(f"{pac}, sua consulta é às {hora}")

consulta("Bianca", "17:30")
consulta()

# Exercício 2

def maior_elemento(n1: int = "1", n2: int = "2", n3: int = "3"):
    print(max(n1, n2, n3))

maior_elemento(1, 45, 87)
maior_elemento(87, 1, 76)


# Parâmetros do tipo *args

def soma_numeros(*args) -> float:  #args virou lista
    soma = 0
    for valor in args:
        soma = soma + valor
    return soma


print(soma_numeros(34, 56))
print(soma_numeros(34, 56, 68))
print(soma_numeros(662, 6634, 564, 46,7,83,9,64,7,89,27,6,52,67,7,864,5664,37))








# Exercicio 3
# Utilizando *args, faça uma função que calcule aa média de diversos números

def media(*args) -> float:
    soma = 0
    qtd = 0
    for valor in args:
        soma = soma + valor
        qtd += 1
    return soma / qtd

media(22, 33, 44)



# Subalgoritmo encadeado
# PROBLEMA: Dados 3 numeros,, calcular os dois maiores

def calcular_media_nota(n1: float, n2: float, n3: float) -> float:
    def verificar_menor_valor(n1: float, n2: float, n3: float) -> float:
        menor = n1
        if n2 < menor:
            menor = n2
        if n3 < menor:
            menor = n3
        return menor

    media = (n1 + n2 + n3 - verificar_menor_valor(n1, n2, n3)) / 2
    return media

print(calcular_media_nota(5, 6, 7))


# Exercício 4
# Calcular a média simples de 3 notas utilizando o subalgoritmo

def media_3notas(n1: float, n2: float, n3: float) -> float:
    def soma(n1: float, n2: float, n3: float) -> float:
        isoma = n1 + n2 + n3
        return isoma

    media = soma(n1, n2, n3) / 3
    return media

print(media_3notas(10, 7, 9))