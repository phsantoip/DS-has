resp = 's'
total = 0
while resp.upper() == 'S':
    comodo = input("Digite o nome do cômodo: ")
    l = input("Digite a largura do cômodo (em m): ")
    c = input("Digite o comprimento do cômodo (em m): ")

    if l.isdigit() and c.isdigit():
        l = float(l)
        c = float(c)
        area = l * c
        total = total + area
        print(f"Nome:{comodo}\nÁrea:{area:.1f}m²\n\n")
        resp = input("Deseja continuar? (s/n): ")
        while resp.upper() != 'S' and resp.upper() != 'N':
            resp = input("\n\nErro, [s]im ou [n]ão?")
    else:
        t1 = l.replace(".","",1)
        t2 = c.replace(".","", 1)
        if t1.isdigit() and t2.isdigit():
            l = float(l)
            c = float(c)
            area = l * c
            total = total + area
            print(f"Nome:{comodo}\nÁrea:{area:.1f}m²\n\n")
            resp = input("\nDeseja continuar? (s/n): ")
            while resp.upper() != 'S' and resp.upper() != 'N':
                resp = input("\n\nErro, [s]im ou [n]ão?")
        else:
            print("Digite números válidos.")
            resp = input("\nDeseja continuar? (s/n): ")
            while resp.upper() != 'S' and resp.upper() != 'N':
                resp = input("\n\nErro, [s]im ou [n]ão?")

print(f"\n\nÁrea total: {total}m²")