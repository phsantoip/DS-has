"""
2. Dados os dias de vida de um usuário, informar quantos anos, meses e dias de vida ele tem
Entrada: 1940		Saída: 5anos, 3meses e 25dias

* Considere o ano com 365 dias e mes com 30 dias """

dias = int(input("Digite seus dias de vida: "))
ano = dias // 365
meses = ano % // 12
dia = meses %// 30  

print(f""" 
Anos:{ano}
Meses:{meses}
Dias:{dia}
""")

