import os
os.system("cls")

def inverter_vetor(v1, v2):
    for i in range (4,-1,-1):
      v2[i] = v1[4 - i]
    print(v1)
    print(v2)
            

v1 = [41, 72, 39, 4, 35]
v2 = [0, 0, 0, 0, 0]

inverter_vetor(v1,v2)