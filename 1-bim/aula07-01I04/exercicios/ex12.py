"""12. Fazer um procedimento chamado 'ordena_vetor_crescente(v)' que ordene de forma crescente o vetor
passado por parâmetro.
	ordena_vetor_crescente(v1)
	>> [4, 35, 39, 41, 72]"""
import os
os.system("cls")
import os
os.system("cls")

def inverter_vetor(v1, v2):
    for i in range (4,-1,-1):
      v2[i] = v1[4 - i]
    
def contarelementos(v1):


def ordena_vetor_crescente(v1):
    n = contarelementos(v1)
    for i in range(n-1):
        for j in range(i+1,n):
            if not inverter_vetor(v1,v2) and v1[i] > v1[j]:
                qtd = v1[i]
                v1[i] = v1[j]
                v1[j] = qtd 
            else:
                qtd = v1[i]
                v1[i] = v1[j]
                v1[j] = qtd 
print(f"seu vetor é {v1}")

v1 = [41, 72, 39, 4, 35]

ordena_vetor_crescente(v1)

# && -> and 
# || -> o


