sal = float(input("Digite seu salário: "))
desc = (sal * 11) / 100
if (desc >= 877):
    desc = 877

sal_final = sal - desc

print(f"Salário Líquido:R${sal:.2f}")
print(f"Desconto:R${desc:0.2f}")
print(f"Salário Final:R${sal_final:.2f}")