def tri() -> None:
    if (n1 > n2 + n3) or (n2 > n1 + n3) or (n3 > n1 + n2):
        print("Estes valores formam um triângulo.")
    else:
        print("Estes valores não formam um triângulo.")

n1 = float(input("Digite um número: "))
n2 = float(input("Digite um número: "))
n3 = float(input("Digite um número: "))

tri()