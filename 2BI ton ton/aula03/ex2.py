print("+ = adição\n"
      "- = subtração\n"
      "x = multiplicação\n"
      "X = multiplicação\n"
      "* = multiplicação\n"
      "/ = divisão inteira\n"
      ": = divisão\n"
      "% = módulo")

sinal = input("Digite o sinal da conta: ")

n1 = float(input("Digite o primeiro numero: "))
n2 = float(input("Digite o segundo numero: "))

match sinal:
    case '+':
        print(n1+n2)
    case '-':
        print(n1-n2)
    case 'x':
        print(n1 * n2)
    case 'X':
        print(n1 * n2)
    case '*':
        print(n1*n2)
    case '%':
        print(n1%n2)
    case '/':
        n1 = int(n1)
        n2 = int(n2)
        print(n1/n2)
    case ':':
        print(n1/n2)
    case _:
        print("Sinal Inválido.")