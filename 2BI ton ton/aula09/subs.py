def retornar_primeiro (vet: list) -> int:
    print("Vetor:")
    print(vet)
    print("\n")
    return  vet[0]

def retornar_negativos (vet: list) -> None:
    print("Vetor:")
    print(vet)
    print("\n")
    for i in range(0, len(vet), 1):
        if vet[i] < 0:
            print(f"{i} = {vet[i]}")

def somar_elementos (vet: list) -> int:
    print("Vetor:")
    print(vet)
    print("\n")
    soma = 0
    for i in range(0, len(vet), 1):
        soma = soma + vet[i]
    return soma

def retornar_media (vet: list) -> float:
    print("Vetor:")
    print(vet)
    print("\n")
    soma = 0
    for i in range(0, len(vet), 1):
        soma = soma + vet[i]
    media = soma / (len(vet))
    return media

def numeros_impares (vet: list) -> None:
    print("Vetor:")
    print(vet)
    print("\n")
    for i in range(0, len(vet), 1):
        if vet[i] % 2 != 0:
            print(f"{i} = {vet[i]}")

def primeiro_ultimo (vet: list) -> None:
    print("Vetor:")
    print(vet)
    print("\n")
    print(f"Primeiro = {vet[0]}")
    print(f"Último = {vet[len(vet) - 1]}")

def indice_par (vet: list) -> None:
    print("Vetor:")
    print(vet)
    print("\n")
    for i in range(0, len(vet), 1):
        if i % 2 == 0:
            print(f"{i} = {vet[i]}")

def verificar_existencia (vet:list) -> bool:
    print("Vetor:")
    print(vet)
    n = float(input("Digite um número: "))
    print("\n")
    t = 0
    for i in range(0, len(vet), 1):
        if vet[i] == n:
            t = 1
    if t > 0:
        return True
    else:
        return False

def ordenar_elementos (vet:list) -> list:
    print("Vetor:")
    print(vet)
    print("\n")
    for i in range(0, len(vet), 1):
        minimo = i
        i2 = i + 1
        while i2 < len(vet):
            if vet[i2] < vet[minimo]:
                minimo = i2
            i2 += 1
        vet[i], vet[minimo] = vet[minimo], vet[i]
    return vet

def copia_vetor (vet: list, vet2:list) -> None:
    print("Antes:")
    print(vet)
    print(vet2)
    print("\n")
    for i in range(0, len(vet), 1):
        vet2[i] = vet[i]
    print("Depois:")
    print(vet)
    print(vet2)

def inverte_vetor (vet:list, vet2:list) -> None:
    print("Antes:")
    print(vet)
    print(vet2)
    print("\n")
    for i in range(0, len(vet), 1):
        vet2[i] = vet[len(vet) - (i + 1)]
    print("Depois:")
    print(vet)
    print(vet2)

def ordena_vetor_crescente (vet:list) -> None:
    print("Antes:")
    print(vet)
    print("\n")
    for i in range(0, len(vet), 1):
        minimo = i
        i2 = i + 1
        while i2 < len(vet):
            if vet[i2] < vet[minimo]:
                minimo = i2
            i2 += 1
        vet[i], vet[minimo] = vet[minimo], vet[i]
    print("Depois:")
    print(vet)

def ordena_vetor_decrescente (vet:list) -> None:
    print("Antes:")
    print(vet)
    print("\n")
    for i in range(0, len(vet), 1):
        minimo = i
        i2 = i + 1
        while i2 < len(vet):
            if vet[i2] > vet[minimo]:
                minimo = i2
            i2 += 1
        vet[i], vet[minimo] = vet[minimo], vet[i]
    print("Depois:")
    print(vet)

def ordena_vetor (vet:list) -> None:
    resp = "s"
    while resp.upper() == "S":
        forma = input("Digite a forma que deseja ordenar (C/D): ")
        if forma == 'd' or forma == 'D':
            ordena_vetor_decrescente(vet)
            resp = "n"
        elif forma == 'C' or forma == 'c':
            ordena_vetor_crescente(vet)
            resp = "n"

def separa_vetor (vet:list) -> None:
    print("Antes:")
    print(vet)
    print("\n")
    dir = len(vet) - 1
    esq = 0
    aux = []
    for p in range(0, len(vet), 1):
        aux.append(p)
        aux[p] = 0
    for i in range(0, len(vet), 1):
        if vet[i] % 2 == 0:
            aux[dir] = vet[i]
            dir -= 1
        else:
            aux[esq] = vet[i]
            esq += 1
    print("Depois:")
    print(aux)

def conta_acima_media (vet:list) -> int:
    soma = 0
    num = 0
    for i in range(0, len(vet), 1):
        soma = soma + vet[i]
    media = soma / (len(vet))
    for i in range(0, len(vet), 1):
        if vet[i] > media:
            num += 1
    return num

def maior_elemento (vet:list) -> int:
    num = vet[0]
    for i in range(0, len(vet), 1):
        if i + 1 != len(vet):
            if vet[i] < vet[i + 1]:
                if num < vet[i + 1]:
                    num = vet[i + 1]
    return num

def busca_vetor (vet:list) -> bool:
    print("Vetor:")
    print(vet)
    n = float(input("Digite um número: "))
    print("\n")
    t = 0
    for i in range(0, len(vet), 1):
        if vet[i] == n:
            t = 1
    if t > 0:
        return True
    else:
        return False