import os 
os.system('cls')

lado1 = float(input("Digite o comprimento do primeiro lado: "))
lado2 = float(input("Digite o comprimento do segundo lado: "))
lado3 = float(input("Digite o comprimento do terceiro lado: "))

if lado1 == lado2 == lado3:
    print("O triangulo é Equilatero")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("O triangulo é Isosceles")
else:
    print("O triangulo é Escaleno")