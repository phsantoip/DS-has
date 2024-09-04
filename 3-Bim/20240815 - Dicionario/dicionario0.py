###
# DICIONÁRIO
# POSSUI CHAVES E VALORES => KEY e VALUE
# KEY => CHAVE 
# VALUE => CONTEÚDO ASSOCIADO À CHAVE
# KEYS => TODAS AS CHAVES
# VALUES => SÃO TODOS OS VALORES
# ITEM => CONJUNTO KEY,VALOR
# ITEMS => SÃO TODOS OS CONJUNTOS DO DICIONÁRIO
###
def exibicao_manual(d: dict) ->None:
    os.system("cls")
    print(f"Nome........: {d['nome']}")
    print(f"Idade.......: {d['idade']}")
    print(f"Casada......: {d['casada']}")

def exibicao_metodos(d: dict) -> None:
    for chave, valor in d.items():
        print(f"{chave} -> {valor}")
import os
os.system("cls")
# CRIANDO UM DICIONÁRIO
dicionario = {} # ou dict
print(dicionario)

contato={
    #'key' : value
    'nome': 'Eliane',
    'idade': 45,
    'casada': True
}
print(contato)
os.system("cls")
print(f"Nome........: {contato['nome']}")
print(f"Idade.......: {contato['idade']}")
print(f"Casada......: {contato['casada']}")



os.system("cls")
#Manipulando as chaves do dicionário
print(contato.keys()) #objeto bruto
print(list(contato.keys()))
for chave in contato.keys():
    print(chave)

os.system("cls")
#Manipular os valores 
print(contato.values())
print(list(contato.values()))
for valores in contato.values():
    print(valores)

os.system("cls")
#Manipular os itens
print(contato.items())
print(list(contato.items())) #Criando uma lista
for chave, valor in contato.items():
    print(f"{chave} -> {valor}")
    
os.system("cls")
contato['altura'] = 1.63
exibicao_metodos(contato)