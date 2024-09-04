def cadastrar_registro(d: dict) -> None:
    for chave in d:
        v = input(f"{chave}:")
        d[chave] = v
        
def exibir_registro(d: dict) -> None:
    for chave in d: 
        tamanho = 15 - len(chave)
        pontos = '.' * tamanho
        print(f"{chave}{pontos}: {d[chave]}")
        
def exibir_registro2(d: dict) -> None:
    d_keys = list(d.keys())
    d_values = list(d.values())
    for c in range(0,len(d_keys),1): 
        tamanho = 15 - len(d_keys[c])
        pontos = '.' * tamanho
        print(f"{d_keys[c]}{pontos}: {d_values[c]}")
    
def exibir_registro3(d: dict) -> None:
    d_items = list(d.items())
    for c in range(0,len(d_items),1):
        t = d_items[c]
        tamanho = 15 - len(t[0])
        pontos = '.' * tamanho
        print(f"{t[0]}{pontos}: {t[1]}")
        
import os
d = {
    'Instagram' : '',
    'Nome'      : '',
    'Idade'     : '',
    'Celular'   : ''
}
resp = 's'
while resp.upper() == 'S':
    os.system("cls")

    print("0 - SAIR\n1 - Cadastrar Registro.\n2 - Exibir Registro.\n3 - Exibir Registro (usando os métodos).\n4 - Exibir Registro (usando o método .items).")
    op = input("\nDigite sua escolha: ")
    match(op):
        case '1':
            cadastrar_registro(d)
            print()
        case '2':
            exibir_registro(d)  #Maneira ja feita
            print()
        case '3':
            exibir_registro2(d) #utilizando .keys() e .values()
            print()
        case '4':
            exibir_registro3(d) #utilizando .items()
        case '0':
            print()
        case _:
            print("Escolha Inválida!")
    if op != '0':
        resp = input("\nDeseja reiniciar o programa? (S/N): ")
        while resp.upper() != "S" and resp.upper() != "N":
            resp = input("ERRO! Digite S ou N: ")
    else:
        resp = 'n'