# =======> SUBALGORITMOS

def preenche_varios(t: list, c: dict) -> None:
    while True:
        print("Preencha o Registro.")
        aux = input("Nome: ")
        if aux == '.':
            break
        else:
            c['nome'] = aux
            c['idade'] = input("Idade: ")
            c['RM'] = input("RM: ")
            c['sala'] = input("Sala: ")
            t.append(c.copy())
        print()
    print("Gravado com Sucesso!")

def exibe_indice(i: int, t: list) -> None:
    if i < len(t) and i >= 0:
        print(f"Nome: {t[i]['nome']}")
        print(f"Idade: {t[i]['idade']}")
        print(f"RM: {t[i]['RM']}")
        print(f"Sala: {t[i]['sala']}")
    else:
        print("Índice Inexistente!")
    input()

def exibe_nome(n: str, t: list) -> None:
    c = 0
    for i in range (0,len(t),1):
        if t[i]['nome'] == n:
            print(f"Nome: {t[i]['nome']}")
            print(f"Idade: {t[i]['idade']}")
            print(f"RM: {t[i]['RM']}")
            print(f"Sala: {t[i]['sala']}")
            c = 1
            break
    if c == 0:
        print("Registro com esse nome não existe!")
    input()

def cadastra_nome(n: str, t: list, c2: dict) -> None:
    c = 0
    for i in range (0,len(t),1):
        if t[i]['nome'] == n:
            print("Esse registro já existe!")
            c = 1
            break
    if c == 0:
        c2['nome'] = n
        c2['idade'] = input("Idade: ")
        c2['RM'] = input("RM: ")
        c2['sala'] = input("Sala: ")
        t.append(c2.copy())
        print("\nGravado com sucesso!")
    input()

def exibir_todos_registros(tabela:list) -> None:
    r = 1
    for i in range(len(tabela)):
        print(f"{r}º Registro!")
        print(f"Nome: {tabela[i]['nome']}")
        print(f"Idade: {tabela[i]['idade']}")
        print(f"RM: {tabela[i]['RM']}")
        print(f"Sala: {tabela[i]['sala']}")
        print()
        r += 1
    input()

def alterar_registro(tabela:list) -> None:
    ind = int(input("Digite o índice: "))
    if ind <= len(tabela) and ind >= 0:
        print(f"Preencha o Registro")
        tabela[ind]['nome'] = input("Nome: ")
        tabela[ind]['idade'] = input("Idade: ")
        tabela[ind]['RM'] = input("RM: ")
        tabela[ind]['sala'] = input("Sala: ")

def deletar_registro(tabela:list) -> None:
    ind = int(input("Digite o índice: "))
    if ind <= len(tabela) and ind >= 0:
        del tabela[ind]

# =======> PRINCIPAL
import os

# definir as estruturas
tabela = list()
contato = {
    'nome': '',
    'idade': '',
    'RM': '',
    'sala': ''
}

while True:
    os.system("cls")
    print("""Menu de Escolhas!
    0 - SAIR
    1 - Preencher os registros até digitar ponto (.)
    2 - Exibir registro pelo índice
    3 - Pesquisar um registro por nome
    4 - Cadastrar um registro consultando o nome
    5 - Listar todos os registros
    6 - Alterar um registro específico (considerando o índice)
    7 - Deletar um registro específico (considerando o índice)
    """)
    opcao = input("Escolha: ")
    match opcao:
        case '0':
            break
        case '1':
            preenche_varios(tabela, contato)
        case '2':
            indice = int(input("Posição: "))
            print()
            exibe_indice(indice, tabela)
        case '3':
            nome = input("Nome: ")
            print()
            exibe_nome(nome, tabela)
        case '4':
            nome = input("Nome: ")
            cadastra_nome(nome, tabela, contato)
        case '5':
            exibir_todos_registros(tabela)
        case '6':
            alterar_registro(tabela)
        case '7':
            deletar_registro(tabela)
        case _:
            print("\nOpção Inválida")
            input()