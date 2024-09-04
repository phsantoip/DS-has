# Dicionario: Estrutura de dados composta por keys (campos) e 
# values (valores)
contato = {}
contato = dict()
contato = {
    # key       : value
    'instagram' : '@edson.edo',
    'nome'      : 'Edson de Oliveira',
    'idade'     : 49
}
import os
# exibindo o dicionario inteiro
print(contato)
# exibindo um elemento do dicionario
print(contato['nome'])
# adicionando uma key a um dicionario existente
contato['celular'] = "11948484848"
os.system("cls")
print(contato)
contato['Nome'] = "Edson oliveira silva"
print(contato)
# removendo uma key
del contato['Nome']
print(contato)
os.system("cls")

def exibe_contato(c: dict) -> None:
    print(f"\nInstagram.: {c['instagram']}")
    print(f"Nome......: {c['nome']}")
    print(f"Celular...: {c['celular']}")
    print(f"Idade.....: {c['idade']}\n")

def exibe_contato2(c: dict) -> None:
    for chave in c:  # chave = instagram
        tamanho = 15 - len(chave)
        pontos = '.' * tamanho
        print(f"{chave}{pontos}: {c[chave]}")
    print()

# exibe_contato(contato)
# contato['salario'] = 848484.84
# exibe_contato(contato)
os.system("cls")
exibe_contato2(contato)
contato['salario'] = 848484.84
exibe_contato2(contato)
os.system("cls")
"""
MÉTODOS DE MANIPULAÇÃO DE DICIONARIOS
keys()      ==> cria uma lista com as chaves
values()    ==> cria uma lista com os valores
items()     ==> seleciona ambos
"""
print(contato.keys())
contato_keys = list(contato.keys())
print(contato_keys)
"""
Crie um dicionário com ao menos 4 campos e apresente o menu:

    0 - SAIR
    1 - Cadastrar Registro  <== FAZER
    2 - Exibir Registro <== FEITO
    3 - Exibir Registro (usando os métodos) <== FAZER
"""


# print(contato.values())
# print(contato.items())



