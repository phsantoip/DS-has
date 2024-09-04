def verificar(nota: float) -> None:
    if nota < 0 or nota > 10:
        print("Nota Inválida.")
    else:
        print("Nota Válida.")

nota = float(input("Insira uma nota: "))
verificar(nota)