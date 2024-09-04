def verificar(nota: float) -> float:
    if nota < 0 or nota > 10:
        resp = "Nota Inválida"
    else:
        resp = "Nota Válida"
    return resp

nota = float(input("Insira uma nota: "))
v = verificar(nota)
print(v)