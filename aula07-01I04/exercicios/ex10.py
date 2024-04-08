import os
os.system("cls")

'''
10. Fazer um procedimento chamado 'copia_vetor(v1, v2)' que copie os elementos do vetor v1 em v2.
	copia(v1, v2)
	>> 45 33
'''


def copia(v1, v2):
    for i in range(0 , 5, 1):
        v2[i] = v1[i]
    return print(v2)

v1 = [41, 72, 39, 4, 35]
v2 = [0, 0, 0, 0, 0] 

copia(v1, v2)      