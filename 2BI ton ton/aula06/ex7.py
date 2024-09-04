def tri():
    if (n1 > n2 +n3) or (n2 > n1 + n3) or (n3 > n1 + n2):
        resp = "Estes valores formam um triângulo."
    else:
        resp = "Estes valores não formam um triângulo."
    return resp

n1 = float(input("Digite um número: "))
n2 = float(input("Digite um número: "))
n3 = float(input("Digite um número: "))

v = tri()
print(v)