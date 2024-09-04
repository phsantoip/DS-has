def converter_horas(h:int) -> str:
    if h > 12:
        t = 'P'
    elif h < 12:
        t = 'A'
    elif h == 12:
        t = 'P'
    return t

def converter_minutos(m:int) -> int:
    m2 = int(m / 60)
    return m2

def sair(h:int, m:int, m2: int, t: str) -> str:
    h = h + m2
    if m >= 60:
        m = m % 60

    if h > 12:
        h = h - 12

    if t == 'P':
        mensagem = print(f"{h}:{m} P.M.")
    elif t == 'A':
        mensagem = print(f"{h}:{m} A.M.")

    return mensagem

resp = 'S'
while resp.upper() == 'S':
    h = int(input("Digite as horas: "))
    m = int(input("Digite os minutos: "))
    t = converter_horas(h)
    m2 = converter_minutos(m)
    print(sair(h, m, m2, t))

    resp = input("Deseja reiniciar o programa? (S/N): ")
    while resp.upper() != 'S' and resp.upper() != 'N':
        resp = input("Erro! Digite corretamente. (S/N): ")

    print("")