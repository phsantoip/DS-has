# AMBIENTE DOS SUBALGORITMOS
# ----- PROCEDIMENTO
def saudacao() -> None:
    print("Boa tarde, Edson!")


def saudacao2(nome: str) -> None:
    print(f"Boa tarde, {nome}!")


def saudacao3(nome: str, hora: int) -> None:
    if hora < 12:
        x = "Bom dia"
    elif hora < 18:
        x = "Boa tarde"
    else:
        x = "Boa noite"
    print(f"{x}, {nome}!")

# ---------- FUNÇÃO
def dobro(n: float) -> float:
    return n + n

# PROGRAMA PRINCIPAL
saudacao()
saudacao2("Ester")
saudacao3("Marion",23)
resp = dobro(6)
print(resp)

"""
EXERCICIOS:
1. Fazer uma função que calcule o cubo de um numero passado por parametro
2. Dada a base e expoente por parâmetro, calcular a potencia através de uma função
3. Dada uma nota por parâmetro, fazer um procedimento que exiba na tela se ela é "Valida" ou "Inválida"
4. Dada uma nota por parâmetro, fazer uma função que retorne é "Valida" ou "Inválida"
5. Dado um número, calcular o seu fatorial
6. Dados 3 valores, informar via procedimento se eles formam um triangulo.
7. Dados 3 valores, informar via função se eles formam um triangulo.

"""