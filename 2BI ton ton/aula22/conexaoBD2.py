import pyodbc
import os
import pandas as pd

repetir = 's'
contato_list = list()
contato = {
    'id': '',
    'nome': '',
    'instagram': '',
    'email': '',
}

dados_conexao = (
    "Driver={SQL Server};"
    "Server=ZETZLOL\\SQLEXPRESS;"
    "Database=PythonSQL;"
    "Trusted_Connection=yes;"
)

conexao = pyodbc.connect(dados_conexao)

cursor = conexao.cursor()
cursor_consulta = conexao.cursor()
cursor_listar = conexao.cursor()

def Lista_Todos(interno: bool) -> dict:
    if not interno:
        os.system('cls')

    lista_dados=list()
        
    cursor_consulta.execute("select * from contato")

    data = cursor_consulta.fetchall()


    for dt in data:
        lista_dados.append(dt)
            
    lista_dados = sorted(lista_dados)
    
    dados_df = pd.DataFrame.from_records(
        lista_dados, columns=['id_contato','nome', 'instagram','email']
    )
    if not interno:
        print(dados_df)
        input("Pressione qualquer tecla para continuar ")
    contato_list = dados_df.to_dict()
    return contato_list

def Verificar_Nome() -> str:
    first = True
    nome = input("Nome: ")
    while not nome.replace(" ","").isalnum():
        if first:
            first = False
            print("\033[A\033[A\033[J")
        else:
            print("\033[2A\033[A\033[J")
        print("Este campo deve ser preenchido.")
        nome = input("Nome: ")

    if not first:
        print("\033[2A\033[A\033[J")
        print(f"Nome: {nome}")
    return nome

def email(digitacao : str) -> str:
    first = True
    while True:
        Arr = False
        Pon = False
        AntArr = False
        EntArrPon = False
        DepPon = False
        MaxPon = False
        falta = list()

        if not first:
            digitacao = input("Email: ")

        if digitacao.find("@") != -1:
            Arr = True
            sepArroba = digitacao.split("@")
            sepPonto = sepArroba[1].split(".")
            if sepArroba[0].upper().isupper():
                    AntArr = True
            if sepArroba[1].replace(".","",2).find(".") == -1:
                    MaxPon = True
            if digitacao.find(".") != -1:
                Pon = True
                if sepPonto[0].upper().isupper():
                    EntArrPon = True
            if sepArroba[1].count(".") == 1 and sepPonto[1].upper().isupper():
                DepPon = True
            if sepArroba[1].count(".") == 2 and sepPonto[2].upper().isupper():
                DepPon = True

        if not Arr:
            falta.append("Ao menos um arroba")
        if not Pon:
            falta.append("Ao menos um ponto")
        if not AntArr:
            falta.append("Ao menos uma letra antes do arroba")
        if not EntArrPon:
            falta.append("Ao menos uma letra entre o arroba e o ponto")
        if not DepPon:
            falta.append("Ao menos uma letra depois do ponto")
        if not MaxPon:
            falta.append("No máximo 2 pontos depois do arroba")
        
        if Arr and Pon and AntArr and EntArrPon and DepPon and MaxPon:
            os.system('cls') 
            return digitacao
        else:
            os.system('cls') 
            falta = "\n".join(falta)
            print(f"O email digitado {digitacao} é inválido\n\nO email deve conter: \n{falta}\n")
            first = False
        
        

def Registrar_Dados() -> None:
    while True:
        os.system('cls')
        id_found = False
        contato_list = Lista_Todos(True)
        print("1 - Registrar\n\nDigite 0 para voltar para o Menu Principal\n\nDados para novo registro:\n")
        contato['id'] = int(input("ID: "))
        if contato['id'] != 0:
            for i in range(0, len(contato_list['id_contato']), 1):
                if contato_list['id_contato'][i] == contato['id']:
                    id_found = True
            if id_found:
                print("Esse ID já foi registrado!")
                input()
            else:
                contato['nome'] = Verificar_Nome()
                if contato['nome'] != '0':
                    contato['instagram'] = input("Instagram: ")
                    if contato['instagram'] != '0':
                        contato['email'] = input("Email: ")
                        if contato['email'] != '0':
                            contato['email'] = email(contato['email'])

                            comando = f"INSERT INTO contato(id_contato, nome, instagram, email) VALUES ('{contato['id']}', '{contato['nome']}', '{contato['instagram']}', '{contato['email']}')"
                            cursor.execute(comando)
                            cursor.commit()
                            print("1 - Registrar\n\nDigite 0 para voltar para o Menu Principal\n\nDados para novo registro:\n")
                            print(f"ID: {contato['id']}\nNome: {contato['nome']}\nInstagram: {contato['instagram']}\nEmail: {contato['email']}")
                            print("\nRegistro gravado!\n")
                            input("Pressione qualquer tecla para continuar ")
                        else:
                            return
                    else:
                        return
                else:
                    return
        else:
            return

def Editar_Dados() -> None:
    os.system('cls')
    id_found = False
    contato_list = Lista_Todos(True)
    print("1 - Editar\n\nDigite 0 para voltar para o Menu Principal\n\n")
    i = Pesquisar(Lista_Todos(True), True)
    if i != '0':
        confirm = input("\n Deseja editar este registro?\n[S]im ou [N]ão ")
        if confirm == 's':
            os.system('cls')
            print("2 - Editar\n\nDigite 0 para voltar para o Menu Principal")
            print("\n----------------------------------------------------------\n")
            print(f"Nome: {contato_list['nome'][0]}\nInstagram: {contato_list['instagram'][0]}\nEmail: {contato_list['email'][0]}")
            print("\n----------------------------------------------------------\n")
            print("Novos dados: \n")
            newID = int(input("ID: "))
            for e in range(0, len(contato_list['id_contato']), 1):
                if contato_list['id_contato'][e] == newID:
                    id_found = True
            if id_found:
                print("Esse ID já foi registrado!")
                input()
            else: 
                newNome = Verificar_Nome()
                if newNome != '0':
                    newInstagram = input("Instagram: ")
                    if newInstagram != '0':
                        newEmail = input("Email: ")
                        if newEmail != '0':
                            newEmail = email(newEmail)
                            comando = f"UPDATE contato SET id_contato = '{newID}', nome = '{newNome}', instagram = '{newInstagram}', email = '{newEmail}' WHERE id_contato = {i}"
                            cursor.execute(comando)
                            cursor.commit()
                            print("2 - Editar\n\nDigite 0 para voltar para o Menu Principal")
                            print("\nRegistro editado!")
                            print(i)
                            print("")
                            print("\n----------------------------------------------------------\n")
                            print(f"ID: {newID}\nNome: {newNome}\nInstagram: {newInstagram}\nEmail: {newEmail}")
                            print("\n----------------------------------------------------------\n")
    Voltar()


def Excluir_Dados(contato_list : list) -> None:
    os.system('cls')
    i = Pesquisar(Lista_Todos(True), True)
    if i != '0':
        confirm = input("\n Deseja excluir este registro?\n[S]im ou [N]ão ")
        if confirm == 's':
            comando = f"DELETE contato WHERE id_contato = {i}"
            cursor.execute(comando)
            cursor.commit()
            os.system('cls')
            print("\nRegistro excluído!")

        Voltar()

def Pesquisar(contato_list : dict, interno : bool) -> str:

    f = 0
    id_list = list()

    repetirPesquisa = '1'

    while repetirPesquisa == '1':
        found = False
        qtd = 0
        os.system('cls')
        escolhido = input("Digite o parâmetro desejado (id_contato/nome/instagram/email): ")
        if(escolhido != 'id_contato' and escolhido != 'nome' and escolhido != 'instagram' and escolhido != 'email'):
            print("Parâmetro Inválido.")
            input()
            break
        valor = input("Digite o valor deste parâmetro: ")
        print("\n----------------------------------------------------------\n")
        for i in range (0, len(contato_list['id_contato']), 1):
            if valor in (str(contato_list[escolhido][i]), contato_list[escolhido][i], contato_list[escolhido][i], contato_list[escolhido][i]):
                qtd = qtd + 1
                print(f"Id: {contato_list['id_contato'][i]}")
                print(f"Nome: {contato_list['nome'][i]}")
                print(f"Instagram: {contato_list['instagram'][i]}")
                print(f"Email: {contato_list['email'][i]}")
                print("\n----------------------------------------------------------\n")
                f = contato_list['id_contato'][i]
                id_list.append(contato_list['id_contato'][i])
                found = True

        if not found:
            print("Registro não encontrado.")

        if interno:
            repetirPesquisa = '2'

        if not interno or not found:
            repetirPesquisa = input("\nDigite sua escolha:\n1 - Pesquisar novamente\n2 - Voltar para o Menu Principal ")
            while repetirPesquisa not in ('1','2'):
                os.system('cls')
                print(f"Pesquisa: {valor}")
                print("\n----------------------------------------------------------\n")
                if found:
                    print(f"Nome: {contato_list[i]['nome']}")
                    print(f"Instagram: {contato_list[i]['instagram']}")
                    print(f"Email: {contato_list[i]['email']}")
                    print("\n----------------------------------------------------------\n")

                    f = i
                else:
                    print("Registro não encontrado.\n")
                print(f"{repetirPesquisa} não é uma escolha válida.")
                repetirPesquisa = input("\nDigite sua escolha:\n1 - Pesquisar novamente\n2 - Voltar para o Menu Principal ")

    if found and interno:
        if qtd <= 1:
            return str(f)
        else:
            id_escol = input(f"Há {qtd} resultados correspondentes à sua pesquisa.\nEscolha o ID desejado: ")
            while not id_escol.isnumeric():
                id_escol = input(f"O ID deve ser um número.\nEscolha o ID desejado: ")
            for i in range(0, len(id_list), 1):
                if int(id_escol) == id_list[i]:
                    return int(id_escol)
            while True:
                id_escol = input("Escolha um ID válido: ")
                for i in range(0, len(id_list), 1):
                    if int(id_escol) == id_list[i]:
                        return int(id_escol)

            

    return str(f)

def Voltar() -> str:
    return input("\nPressione qualquer tecla para voltar ao Menu Principal")

while repetir == 's':
    os.system('cls')
    print("1 - Registrar\n2 - Editar\n3 - Excluir\n4 - Pesquisar\n5 - Listar\n0 - Sair")
    choice = int(input("Digite a escolha: "))

    match(choice):
        case 0:
            break
        case 1:
            Registrar_Dados()

        case 2:
            Editar_Dados()

        case 3:
            Excluir_Dados(contato_list)

        case 4:
            Pesquisar(Lista_Todos(True), False)

        case 5:
            Lista_Todos(False)

        case _:
            os.system('cls')
            print(f"{choice} não é uma escolha válida\nDigite uma escolha válida.\n")


''' SCIRPT SQLSERVER
create database PythonSQL
use PythonSQL;
create table contato(
	id_contato int primary key,
	nome varchar(30),
	instagram varchar(30),
	email varchar(30),
)

create database PythonSQL;
use PythonSQL;
create table contato(
	id_contato int primary key,
	nome varchar(30),
	instagram varchar(30),
	email varchar(30));
select * from contato;

Dupla: Arthur de Jesus Lima / Diego F. Blanco
'''