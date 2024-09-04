def cadastrar_dados(id_list:list, id_contato:int):
    while True:
        print(f"\nId = {len(id_list) + 1}")
        aux = input("Nome: ")
        if aux == '.':
            break
        else:
            nome = aux
            instagram = input("Instagram: ")
            email = input("Email: ")
            comando = f"INSERT INTO contato(id_contato, nome, instagram, email) VALUES ({len(id_list) + 1}, '{nome}', '{instagram}', '{email}')"
            cursor.execute(comando)
            id_contato = len(id_list) + 1
            cursor.commit()
            id_list.append(id_contato)
            id_contato += id_contato
            print("Coluna de dados inserida!")
    input("\nAperte Enter para retornar")
        
def alterar_dados(id_list:list):
    c = 0
    aux = int(input("Id_contato: "))
    for i in range(0,len(id_list),1):
        if aux == id_list[i]:
            nome = input("Nome: ")
            instagram = input("Instagram: ")
            email = input("Email: ")
            comando = f"UPDATE contato SET nome = '{nome}', instagram = '{instagram}', email = '{email}' WHERE id_contato = {aux}"
            cursor.execute(comando)
            cursor.commit()
            c = 1
            print("Coluna de dados alterada!")
    
    if c == 0:
        print("Id não encontrado!")
    input("\nAperte Enter para retornar")
        
def excluir_coluna(id_list:list):
    c = 0
    aux = int(input("Id_contato: "))
    for i in range(0,len(id_list)-1,1):
        if aux == id_list[i]:
            id_contato = aux
            comando = f"DELETE FROM contato WHERE id_contato = {id_contato}"
            cursor.execute(comando)
            cursor.commit()
            id_list.remove(id_contato)
            c = 1
            print("Coluna de dados excluída!")
            
    if c == 0:
        print("Id não encontrado!")
    input("\nAperte Enter para retornar")
        
import pyodbc
import os;
dados_conexao = (
    "Driver={SQL Server};"
    "Server=localhost;"
    "Database=PythonSQL;"
    "User='sa';"
    "Password=123456;"
)
conexao = pyodbc.connect(dados_conexao)
cursor = conexao.cursor()

x = 0
id_list = []
id_contato = 1
while True:
    os.system('cls')
    linha = '-------------------------------------------------------------'
    print(f"""
{linha}
Menu de Escolhas!
0 - Sair
1 - Cadastrar dados na tabela (digite '.' no campo 'nome' para terminar)
2 - Alterar dados de uma tabela específica (através do id)
3 - Excluir uma coluna específica (através do id)
{linha}
    """)
    opcao = input("Digite sua escolha: ")
    match(opcao):
        case '0':
            break
        case '1':
            cadastrar_dados(id_list, id_contato)
        case '2':
            alterar_dados(id_list)
        case '3':
            excluir_coluna(id_list)
        case _:
            print("Opção Inválida")
            input()