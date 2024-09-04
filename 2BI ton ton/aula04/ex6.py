resp = 's'
while resp.upper() == 'S':
    classe = input("Digite o número de alunos da classe: ")
    if classe.isdigit():
        classe = int(classe)
        i = 1
        media_classe = 0
        total_media = 0
        aprovados = 0
        reprovados = 0
        while i <= classe:
            n1 = input(f"Digite a primeira nota do {i}º aluno(a): ")
            n2 = input(f"Digite a segunda nota do {i}º aluno(a): ")
            n3 = input(f"Digite a terceira nota do {i}º aluno(a): ")
            if n1.isdigit() and n2.isdigit() and n3.isdigit():
                n1 = float(n1)
                n2 = float(n2)
                n3 = float(n3)
                if n1 > 10 or n1 < 0 or n2 > 10 or n2 < 0 or n3 > 10 or n3 < 0:
                    print("Alguma nota está inválida, digite novamente suas notas!\n")
                    continue
                media = (n1 + n2 + n3) / 3
                i = i + 1
                print(f"Média: {media:.1f}\n")
                total_media = total_media + media
                if media >= 5 and media <= 10:
                    aprovados = aprovados + 1
                elif media < 5:
                    reprovados = reprovados + 1
                else:
                    print("Média Inválida (Lembre-se que as notas são de 0 a 10!)")
            else:
                sol1 = n1.replace(".","",1)
                sol2 = n2.replace(".","",1)
                sol3 = n3.replace(".","",1)
                if sol1.isdigit() and sol2.isdigit() and sol3.isdigit():
                    n1 = float(n1)
                    n2 = float(n2)
                    n3 = float(n3)
                    if n1 > 10 or n1 < 0 or n2 > 10 or n2 < 0 or n3 > 10 or n3 < 0:
                        print("Alguma nota está inválida, digite novamente suas notas!\n")
                        continue
                    media = (n1 + n2 + n3) / 3
                    i = i + 1
                    print(f"Média: {media:.1f}\n")
                    total_media = total_media + media
                    if media >= 5 and media <= 10:
                        aprovados = aprovados + 1
                    elif media < 5:
                        reprovados = reprovados + 1
                    else:
                        print("Média Inválida (Lembre-se que as notas são de 0 a 10!)")
                else:
                    print("Média Inválida (Lembre-se que as notas são de 0 a 10!)\n")
                    continue
    else:
        print("Número Inválido\n")
        continue

    media_classe = total_media / classe
    print(f"\nMédia da classe: {media_classe:.1f}\nNúmero de reprovados: {reprovados}.\nNúmero de aprovados: {aprovados}.")

    resp = input("\nDeseja continuar? (s/n): ")
    while resp.upper() != 'S' and resp.upper() != 'N':
        resp = input("\nErro, [s]im ou [n]ão?")