def valorPagamento(prestacao: float, dias: int) -> float:
    if dias >= 1:
        m = dias * (prestacao * 0.1 / 100)
        valor = prestacao + (prestacao * 3 / 100) + m
    else:
        valor = prestacao
    return valor


prestacao = 1
p = 0
t = 0
while prestacao != 0:
    prestacao = float(input("Informe o valor da prestação: "))
    if prestacao == 0:
        break
    dias = int(input("Informe o número de dias em atraso: "))
    v = valorPagamento(prestacao, dias)
    print(f"O valor a ser pago é de: R${v:.2f}")
    t = float(t + v)
    p = int(p + 1)
    print("")

print(f"\n\nRelatório do dia:\nQuantidade de prestações pagas hoje: {p}\nO Valor total das prestações pagas hoje: R${t:.2f}")