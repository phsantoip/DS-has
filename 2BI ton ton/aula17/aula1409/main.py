#PARTE 1
def checar_email(email:str) -> str:
    c = 0
    c2 = 0
    p = 0
    m = ""
    email = email + " "
    f = email.find("@")
    if f != -1: 
        f2 = email.find(".",f,-1)
    else:
        f2 = email.find(".",0,-1)
    l = f2 + 1
    g = f - 1
    
    #1
    if f == -1  or f2 == -1:
        m = m + "\n-O email deve ter no mínimo um arroba e um ponto."

    #2
    if f != -1:
        if f == 0:
            g = f
        if email[g].isalpha() == False or f == 0:
            m = m + "\n-O email deve ter uma letra antes do arroba."
            
        #5
        p = email[f:-1]
        p = p.split(".")
        if len(p) > 3:
            m = m + "\n-O email deve ter no máximo dois pontos depois do arroba."
        
    if f2 != -1:
        #4            
        if email[l].isalpha() == False:
            m = m + "\n-O email deve ter uma letra depois do ponto."
        
    #3
    if f != -1  and f2 != -1:
        while c < f2 - f:
            c+=1
            if email[f+c].isalpha():
                c2 = 1
        if c2 != 1:
            m = m + "\n-O email deve ter no mínimo uma letra depois do arroba e antes do ponto."
        
    return m

#PARTE 2:
def checar_senha(senha:str) -> str:
    m = ""
    d = 0
    d1 = 0
    d2 = 0
    d3 = 0
    #1
    if len(senha) < 6:
        m = m + "\n-A senha deve ter ao menos 6 caracteres."
        
    while d < len(senha):
        if senha[d].isupper() == True:
            d1 += 1
        if senha[d].isdigit() == True:
            d2 += 1
        if senha[d].isalpha() == False and senha[d].isdigit() == False:
            d3 += 1
        d+=1    
        
    #2
    if d1 == 0:
        m = m + "\n-A senha deve ter ao menos uma letra maiúscula."
        
    #3        
    if d2 == 0:
        m = m + "\n-A senha deve ter ao menos um número."
        
    #4
    if d3 == 0:
        m = m + "\n-A senha deve ter ao menos um caractere especial."
    
    return m

import os
resp = "s"
while resp.upper() == "S":
    os.system("cls")
    print("Cadastrar-se no Sistema!")
    email=input("Digite seu E-mail:\n")
    email2 = checar_email(email)        
    senha=input("\n\nDigite sua Senha:\n")
    senha2 = checar_senha(senha)
    if email2 != "":
        print(f"\nProblemas envolvendo o email: {email2}")
        
    if senha2 == "":
        senha3=input("Digite a Senha novamente:\n")
        if senha3 != senha:
            print(f"Senhas não coincidem!")
    else:
        print(f"\nProblemas envolvendo a senha: {senha2}")
        
    if email2 == "" and senha2 == "" and senha3 == senha:
        print("\nCadastro realizado com sucesso!")
    
    resp = input("\nDeseja reiniciar o programa? (S/N): ")
    while resp.upper() != "S" and resp.upper() != "N":
        resp = input("ERRO! Digite S ou N: ")