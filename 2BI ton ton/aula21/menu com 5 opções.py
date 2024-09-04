def cadastrar_dados(id_list:list, dicio:dict):
    aux = 0
    if len(id_list) == 0:
        dicio['id_contato'] = input("Id: ")
        dicio['nome'] = input("Nome: ")
        dicio['instagram'] = input("Instagram: ")
        dicio['email'] = input("Email: ")
        comando = f"INSERT INTO contato(id_contato, nome, instagram, email) VALUES ({dicio['id_contato']}, '{dicio['nome']}', '{dicio['instagram']}', '{dicio['email']}')"
        cursor.execute(comando)
        cursor.commit()
        id_list.append(dicio.copy())
        print("Coluna de dados inserida!")
    else:
        x = input("Id: ")
        for i in range(0,len(id_list), 1):
            if x == id_list[i]['id_contato']:
                print("Id já cadastrado!")
                aux = 1
                break
        if aux == 0:
            dicio['id_contato'] = x
            dicio['nome'] = input("Nome: ")
            dicio['instagram'] = input("Instagram: ")
            dicio['email'] = input("Email: ")
            comando = f"INSERT INTO contato(id_contato, nome, instagram, email) VALUES ({dicio['id_contato']}, '{dicio['nome']}', '{dicio['instagram']}', '{dicio['email']}')"
            cursor.execute(comando)
            cursor.commit()
            id_list.append(dicio.copy())
            print("Coluna de dados inserida!")
    input("\nAperte Enter para retornar")

def consultar_id(id_list:list):
    aux = 0
    if len(id_list) == 0:
        print("Deve-se cadastrar um registro primeiramente!")
    else:
        x = input("Id: ")
        for i in range(0,len(id_list), 1):
            if x == id_list[i]['id_contato']:
                print()
                print(f"Id: {id_list[i]['id_contato']}")
                print(f"Nome: {id_list[i]['nome']}")
                print(f"Instagram: {id_list[i]['instagram']}")
                print(f"Email: {id_list[i]['email']}")
                comando = f"select * from contato WHERE id_contato = {id_list[i]['id_contato']}"
                cursor.execute(comando)
                cursor.commit()
                print("Coluna de dados exibida!")
                aux = 1
                break
        if aux == 0:
            print("Id não encontrado!")
    input("\nAperte Enter para retornar")

def listar_dados(id_list:list):
    if len(id_list) == 0:
        print("O ideal é que os registros sejam cadastrados primeiramente!")
    else:
        comando = f"select * from contato"
        cursor.execute(comando)
        cursor.commit()
        for i in range(0, len(id_list), 1):
            print(f"{i+1}º Registro!")
            print(f"Id: {id_list[i]['id_contato']}")
            print(f"Nome: {id_list[i]['nome']}")
            print(f"Instagram: {id_list[i]['instagram']}")
            print(f"Email: {id_list[i]['email']}")
            print()
        print("Todas as colunas de dados exibidas!")
    input("\nAperte Enter para retornar")
        
def alterar_dados(id_list:list):
    aux = 0
    if len(id_list) == 0:
        print("Deve-se cadastrar um registro primeiramente!")
    else:
        x = input("Id: ")
        for i in range(0,len(id_list), 1):
            if x == id_list[i]['id_contato']:
                id_list[i]['nome'] = input("Nome: ")
                id_list[i]['instagram'] = input("Instagram: ")
                id_list[i]['email'] = input("Email: ")
                comando = f"UPDATE contato SET nome = '{id_list[i]['nome']}', instagram = '{id_list[i]['instagram']}', email = '{id_list[i]['email']}' WHERE id_contato = {id_list[i]['id_contato']}"
                cursor.execute(comando)
                cursor.commit()
                print("Coluna de dados alterada!")
                aux = 1
                break
        if aux == 0:
            print("Id não encontrado!")
    input("\nAperte Enter para retornar")
    
def excluir_coluna(id_list:list):
    aux = 0
    if len(id_list) == 0:
        print("Deve-se cadastrar um registro primeiramente!")
    else:
        x = input("Id: ")
        for i in range(0,len(id_list), 1):
            if x == id_list[i]['id_contato']:
                id_list.remove(id_list[i])
                comando = f"DELETE FROM contato WHERE id_contato = {x}"
                cursor.execute(comando)
                cursor.commit()
                print("Coluna de dados excluída!")
                aux = 1
                break
        if aux == 0:
            print("Id não encontrado!")
    input("\nAperte Enter para retornar")
        
import pyodbc
import os
import pandas
dados_conexao = (
    "Driver={SQL Server};"
    "Server=ZETZLOL\\SQLEXPRESS;"
    "Database=PythonSQL;"
    "Trusted_Connection=yes;"
)
conexao = pyodbc.connect(dados_conexao)
cursor = conexao.cursor()

x = 0
id_list = []
dicio = {
    "id_contato": "",
    "nome": "",
    "instagram": "",
    "email": "" 
}
id_contato = 1
while True:
    os.system('cls')
    linha = '-------------------------------------------------------------'
    print(f"""
{linha}
Menu de Escolhas!
0 - Sair
1 - Cadastrar dados em um registro.
2 - Consultar um registro acordo com o ID.
3 - Listar todos os registros.
4 - Editar dados de um registro específico (através do ID).
5 - Excluir um registro específico (através do ID).
{linha}
    """)
    opcao = input("Digite sua escolha: ")
    match(opcao):
        case '0':
            break
        case '1':
            print()
            cadastrar_dados(id_list, dicio)
        case '2':
            print()
            consultar_id(id_list)
        case '3':
            print()
            listar_dados(id_list)
        case '4':
            print()
            alterar_dados(id_list)
        case '5':
            print()
            excluir_coluna(id_list)
        case _:
            print("Opção Inválida")
            input()