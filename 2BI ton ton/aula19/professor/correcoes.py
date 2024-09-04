# =======> SUBALGORITMOS

def preenche_varios(t: list, c: dict) -> None:
    while True:
        aux = input("Nome: ")
        if aux == '.':
            break
        else:
            c['nome'] = aux
            c['idade'] = input("Idade: ")
            t.append(c.copy())

def exibe_indice(i: int, t: list) -> None:
    if i < len(t) and i >= 0:
        print(f"Nome: {t[i]['nome']}")
        print(f"Idade: {t[i]['idade']}")
    else:
        print("Inexistente!")
    input()


# =======> PRINCIPAL
import os

# definir as estruturas
tabela = list()
contato = {
    'nome': '',
    'idade': ''
}

while True:
    os.system("cls")
    print("""
    0 - SAIR
    1 - Preencher até digitar ponto (.)
    2 - Exibir registro pelo índice
    3 - Pesquisar por nome
        # cenário 1  
        Nome: Edson
          Nome: Edson
          idade: 49

        # cenário 2  
        Nome: Edson
          Nome não existe
          
    4 - cadastrar consultando
        # cenário 2   
        Nome: Edson
          Nome: Edson
          idade: 49
        Este registro já existe!

        # cenário 2  
        Nome: Edson
          idade: 49
        Gravado com sucesso!

    """)
    opcao = int(input("Escolha: "))
    match opcao:
        case 0:
            break
        case 1:
            preenche_varios(tabela, contato)
        case 2:
            
            indice = int(input("Posição: "))
            exibe_indice(indice, tabela)




print(tabela)