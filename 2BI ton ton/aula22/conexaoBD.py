import pyodbc
dados_conexao = (
    "Driver={SQL Server};"
    "Server=localhost;"
    "Database=PythonSQL;"
    "User='sa';"
    "Password=123456;"
)
'''
    "Driver={SQL Server};"
    "Server=ZETZLOL\\SQLEXPRESS;"
    "Database=PythonSQL;"
    "Trusted_Connection=yes;"
'''

conexao = pyodbc.connect(dados_conexao)
print("Conexão Bem Sucedida")

cursor = conexao.cursor()


id_contato = 3
nome = "Jeniffer"
instagram = "@jeniffer"
email = "jeniffer@hotmail.com"

comando = f"INSERT INTO contato(id_contato, nome, instagram, email) VALUES ({id_contato}, '{nome}', '{instagram}', '{email}')"

cursor.execute(comando)
cursor.commit()

print("registro gravado")


''' SCIRPT SQLSERVER
create database PythonSQL;
use PythonSQL;
create table contato(
	id_contato int primary key,
	nome varchar(30),
	instagram varchar(30),
	email varchar(30),
);
'''