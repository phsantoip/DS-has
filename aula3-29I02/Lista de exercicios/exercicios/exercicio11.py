import os 
os.system('cls')

angulo1 = float(input("Digite o valor do primeiro angulo: "))
angulo2 = float(input("Digite o valor do segundo angulo: "))
angulo3 = float(input("Digite o valor do terceiro angulo: "))

if angulo1 + angulo2 + angulo3 == 180:
    if angulo1 < 90 and angulo2 < 90 and angulo3 < 90:
        print("O triangulo é Actangulo")
    elif angulo1 == 90 or angulo2 == 90 or angulo3 == 90:
        print("O triangulo é Retangulo")
else:
        print("O triangulo é Obtusangulo")
    