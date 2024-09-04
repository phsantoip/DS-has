tabela = list()
contato = {
    'nome': '',
    'idade': 0,
    'telefone':''
}

# preenchimento do dicionario
contato['nome'] = input("Nome: ")
contato['idade'] = int(input("Idade: "))
contato['telefone'] = input("Telefone: ")
tabela.append(contato.copy())
print(contato)
print(tabela)

contato['nome'] = input("\nNome: ")
contato['idade'] = int(input("Idade: "))
contato['telefone'] = input("Telefone: ")
tabela.append(contato.copy())

print(contato)
print(tabela)

for i in range(0, len(tabela), 1):
    print(f"Nome: {tabela[i]['nome']}")
    print(f"Idade: {tabela[i]['idade']}")
    print(f"Telefone: {tabela[i]['telefone']}")


"""
Exercícios:
. Criar um dicionário com ao menos 4 keys e:

    1 - Preencher a tabela (até que seja digitado . na primeira key)
    2 - Exibir um registro específico (considere o índice)
    3 - Exibir todos os registros da Tabela

Para todos aplique subalgoritmos.



"""
