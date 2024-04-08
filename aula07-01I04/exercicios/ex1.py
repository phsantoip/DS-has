import os
os.system("cls")

def primero_elm(vetor):
    if vetor:
        return vetor[0]
    else:
        return None
vetor = [45, -89, 32, -12, 32]
primeiro = primero_elm(vetor)
print(" primeiro elemento eh:")