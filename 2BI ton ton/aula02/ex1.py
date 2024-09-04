peso = float(input("Digite seu peso (em kg): "))
altura = float(input("Digite seu altura (em m): "))

media = peso / (altura * altura)

if(altura > 3.00 or peso > 600):
    print("Alguma medida está inválida, lembre-se que os valores que devem ser colocados em m e kg.")
else:
    if (media < 18.5):
        print("Magreza")
    elif (media >= 18.5 and media <=24.9):
        print("Normal")
    elif (media >= 25 and media <=29.9):
        print("Sobrepeso")
    elif (media >= 30 and media <=34.9):
        print("Obesidade grau I")
    elif (media >= 35 and media <=39.9):
        print("Obesidade grau II")
    else:
        print("Obesidade grau III")