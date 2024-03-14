import os
os.system("cls")

macas = int(input("Digite quantas maças você deseja: "))

if macas >= 12:
    pre = 0.25
else:
    pre = 0.30

valor = pre * macas    

print(f"o valor da sua compra saira: {valor}")