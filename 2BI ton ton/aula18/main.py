def preencher_tabela(tabela:list, registro:dict) -> list:
    while True:
        print(f"Preencha o Registro.")
        registro['Nome'] = input("Nome: ")
        if registro['Nome'] == ".":
            break
        registro['Idade'] = input("Idade: ")
        registro['Nacionalidade'] = input("Nacionalidade: ")
        registro['Estado Civil'] = input("Estado Civil: ")
        tabela.append(registro.copy())
        print()
    return tabela
    
def exibir_registro(tabela:list, indice:int) -> None:
    if indice <= len(tabela) and indice >= 0:
        print(f"Nome: {tabela[indice-1]['Nome']}")
        print(f"Idade: {tabela[indice-1]['Idade']}")
        print(f"Nacionalidade: {tabela[indice-1]['Nacionalidade']}")
        print(f"Estado Civil: {tabela[indice-1]['Estado Civil']}")
        print()
    else:
        print("ìndice não encontrado")

def exibir_todos_registros(tabela:int) -> None:
    r = 1
    for i in range(len(tabela)):
        print(f"{r}º Registro!")
        print(f"Nome: {tabela[i]['Nome']}")
        print(f"Idade: {tabela[i]['Idade']}")
        print(f"Nacionalidade: {tabela[i]['Nacionalidade']}")
        print(f"Estado Civil: {tabela[i]['Estado Civil']}")
        print()
        r += 1

import os
resp = 's'
tabela = []
registro = {
    'Nome': '',
    'Idade': 0,
    'Nacionalidade': '',
    'Estado Civil': ''
}
while resp.upper() == 'S':
    os.system("cls")
    print("Menu de Escolha!")
    print("1 - Preencher a tabela (até que seja digitado . na primeira key)")
    print("2 - Exibir um registro específico (considerando o índice)")
    print("3 - Exibir todos os registros da Tabela\n")
    op = input("Digite sua opção:")
    print()
    match(op):
        case '1':
            preencher_tabela(tabela, registro)
        case '2':
            i = int(input("Digite um registro específico a ser exibido: "))
            exibir_registro(tabela,i)
        case '3':
            exibir_todos_registros(tabela)
        case _:
            print("Opção Inválida!")

    if op != '1':
        resp = input("Deseja reiniciar o programa? (S/N)")
        while resp.upper() != 'S' and resp.upper() != 'N':
            resp = input("Erro! Digite S ou N: ")