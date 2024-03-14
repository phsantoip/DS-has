import os
os.system("cls")
"""
    EXERCÍCIO:
Uma sala de aula tem 10 alunos.
A média semestral se dá pela média simples entre 3 notas, descartando
a de menor valor.
A cada nota digitada, verificar se ela está entre 0 e 10 (inclusive),
se não estiver exiba "Nota inválida" e peça para digitar novamente, caso
contrário, vá para a próxima nota.
No final, mostre a média da sala e quantos tiraram ao menos 9 de media.
    """

alunos = [10]

for aluno in range(1,10,1):
#aluno 1 nota
    while True:
        nota1 = float(input("Digite a primeira nota do aluno: "))
        if nota1 < 0 or nota1  > 10:
            print("Nota invalida")
        else:
            print("proxima Nota")
        break
#aluno 2 nota
    while True:
        nota2 = float(input("Digite a segunda nota do aluno: "))
        if nota2 < 0 or nota2  > 10:
            print("Nota invalida")
        else:
            print("proxima Nota")
        break
    

  

