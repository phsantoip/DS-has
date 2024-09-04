#1
def conta_palavras(frase: str) -> int:
    return len(frase.split())

def substituir(frase: str, elemento: str) -> str:
    i = frase.replace(elemento,elemento.upper())
    return i

def exibir_por_numero(frase:str, numero:int) -> str:
    f = frase.split()
    return f[numero-1]


nome = "edson de oliveira enzo"
print(f"Nome = {nome}")
print(f"\nO número de palavras no nome é: {conta_palavras(nome)}")
elemento = input("Digite um elemento: ")
print(f"\nNome com a letra maiúscula alterada = {substituir(nome, elemento)}")
numero = int(input("Digite um numero: "))
print(f"A palavra correspondente ao número é: {exibir_por_numero(nome, numero)}")
