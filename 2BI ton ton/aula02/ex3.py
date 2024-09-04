p1 = float(input("Digite a nota da sua primeira prova: "))
p2 = float(input("Digite a nota da sua segunda prova: "))
p3 = float(input("Digite a nota da sua terceira prova: "))
mp = (p1 + p2 + p3) / 10

t1 = float(input("Digite a nota do seu primeiro trabalho: "))
t2 = float(input("Digite a nota do seu segundo trabalho: "))
mt = (t1 + t2) / 2
mt = (mt * 3) / 10

proj = float(input("Digite a nota do seu projeto: "))
proj = (proj * 4) / 10

media = mp + mt + proj

if(p1 > 10 or p2 > 10 or p3 > 10 or t1 > 10 or t2 > 10 or proj > 10 or p1 < 0 or p2 < 0 or p3 < 0 or t1 < 0 or t2 < 0 or proj < 0):
    print("Alguma nota está inválida, verifique novamente suas notas.")
else:
    if (media < 4):
        print("Reprovado sem direito a recuperação")

    elif (media >= 4 and media < 7):
        rec = float(input("Digite a nota da recuperação: "))
        media = ((rec + media) / 2)
        if (media >= 6):
            print("Aluno aprovado após recuperação")
        else:
            print("Aluno reprovado")

    elif (media >= 7):
        print("Aluno aprovado")
    else:
        print("Média Inválida (Verifique se digitou suas notas corretamente)")