import pyodbc
import os
import pandas as pd


def cadastro_contato():

    id_contato = 4
    nome = "edson"
    instagram = "@eds"
    email = "eds@hotmail.com"

    comando = f"INSERT INTO contato(id_contato, nome, instagram, email) VALUES ({id_contato}, '{nome}', '{instagram}', '{email}')"

    cursor_cadastro.execute(comando)
    cursor_cadastro.commit()

    print("registro gravado")

# DADOS DA CONEXAO
dados_conexao = (
    "Driver={SQL Server};"
    "Server=localhost;"
    "Database=PythonSQL;"
    "User='sa';"
    "Password=123456;"
)

conexao = pyodbc.connect(dados_conexao)
cursor_cadastro = conexao.cursor()
cursor_consulta = conexao.cursor()
cursor_listar = conexao.cursor()
print("Conexão Bem Sucedida")

os.system("cls")

print("""
      1 - Cadastro
      2 - Consultar 
      3 - listar todos
      """)
opcao = int(input("Escolha: "))
match opcao:
    case 1:
        cadastro_contato()
    case 2:
        lista_dados=list()
        id = int(input("Digite o ID: "))
        cursor_consulta.execute(f"select * from contato where id_contato = {id}")

        data = cursor_consulta.fetchall() # armazenar varios registros

        if len(data) == 0:
            print("Não existe")
        else:
            # existe
            for dt in data:
                lista_dados.append(dt)
            
            lista_dados = sorted(lista_dados) # ordena a lista

            #print(lista_dados)

            dados_df = pd.DataFrame.from_records(
                lista_dados, columns=['id_contato','nome', 'instagram','email'], index = 'id_contato'
            )
            print(dados_df)
    case 3:
        lista_dados=list()
        
        cursor_consulta.execute("select * from contato")

        data = cursor_consulta.fetchall()

        if len(data) == 0:

            print("Não existe")
        else:

            for dt in data:
                lista_dados.append(dt)
            
            lista_dados = sorted(lista_dados)
            #print(lista_dados)
            dados_df = pd.DataFrame.from_records(
                 lista_dados, columns=['id_contato','nome', 'instagram','email'], index = 'id_contato'
            )
            print(dados_df)

    case 4:
        lista_dados=list()
        id = int(input("Digite o ID: "))
        cursor_consulta.execute(f"select * from contato id_contato = {id}")

        data = cursor_consulta.fetchall()

        if len(data) == 0:

            print("Não existe")
        else:

            for dt in data:
                lista_dados.append(dt)
            
            lista_dados = sorted(lista_dados)
            print(lista_dados)
            dados_df = pd.DataFrame.from_records(
                lista_dados, columns=['id_contato','nome', 'instagram','email'], index = 'id_contato'
            )
            print(dados_df)




    


''' SCIRPT SQLSERVER
create database PythonSQL
use PythonSQL;
create table contato(
	id_contato int primary key,
	nome varchar(30),
	instagram varchar(30),
	email varchar(30),
);
'''