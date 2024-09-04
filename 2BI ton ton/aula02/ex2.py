sal = float(input("Digite seu salário: "))

if (sal < 1903.98):
    print(f"Alíquota: Isento")
elif (sal >= 1903.99 and sal <=2826.65):
    alq = (sal * 7.5) / 100
    print(f"Alíquota: R${alq:.2f}")
elif (sal >= 2826.66 and sal <=3751.05):
    alq = (sal * 15) / 100
    print(f"Alíquota: R${alq:.2f}")
elif (sal >= 3751.06 and sal <=4664.68):
    alq = (sal * 22.5) / 100
    print(f"Alíquota: R${alq:.2f}")
else:
    alq = (sal * 27.5) / 100
    print(f"Alíquota: R${alq:.2f}")