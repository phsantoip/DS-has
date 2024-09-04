def cadastrar_dados(id_list:list, x:int):
    if x == 0:
        id_contato = int(input("Id_contato: "))
        nome = input("Nome: ")
        instagram = input("Instagram: ")
        email = input("Email: ")
        comando = f"INSERT INTO contato(id_contato, nome, instagram, email) VALUES ({id_contato}, '{nome}', '{instagram}', '{email}')"
        cursor.execute(comando)
        cursor.commit()
        id_list.append(id_contato)
    print()
    c = 0
    aux = int(input("Id_contato: "))
    for i in range(0,len(id_list),1):
        if aux == id_list[i]:
            print("Este id já foi cadastrado!")
            c = 1
            input()
            break
    if c == 0:
        id_contato = aux
        nome = input("Nome: ")
        instagram = input("Instagram: ")
        email = input("Email: ")
        comando = f"INSERT INTO contato(id_contato, nome, instagram, email) VALUES ({id_contato}, '{nome}', '{instagram}', '{email}')"
        cursor.execute(comando)
        cursor.commit()
        id_list.append(id_contato)
        print()
        
def alterar_dados(id_list:list):
    c = 0
    aux = int(input("Id_contato: "))
    for i in range(0,len(id_list),1):
        if aux == id_list[i]:
            id_contato = aux
            nome = input("Nome: ")
            instagram = input("Instagram: ")
            email = input("Email: ")
            comando = f"UPDATE contato SET nome = '{nome}', instagram = '{instagram}', email = '{email}' WHERE id_contato = {id_contato}"
            cursor.execute(comando)
            cursor.commit()
            c = 1
            print()
            
    if c == 0:
        print("Id não encontrado!")
        input()
        
def excluir_coluna(id_list:list):
    c = 0
    aux = int(input("Id_contato: "))
    for i in range(0,len(id_list),1):
        if aux == id_list[i]:
            id_contato = aux
            comando = f"DELETE FROM contato WHERE id_contato = {id_contato}"
            cursor.execute(comando)
            cursor.commit()
            id_list.remove(id_contato)
            c = 1
            print()
            
    if c == 0:
        print("Id não encontrado!")
        input()
        
import pyodbc
import os;
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
while True:
    os.system('cls')
    print("""Menu de Escolhas!
        0 - Sair
        1 - Cadastrar dados na tabela
        2 - Alterar dados de uma tabela específica (através do id)
        3 - Excluir uma coluna específica (através do id)
        """)
    opcao = input("Digite sua escolha: ")
    match(opcao):
        case '0':
            break
        case '1':
            cadastrar_dados(id_list, x)
            x += 1
        case '2':
            alterar_dados(id_list)
        case '3':
            excluir_coluna(id_list)
        case _:
            print("Opção Inválida")
            input()