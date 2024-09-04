tabela = []

contato = {
    'nome': 'Edson',
    'idade': '50'
}
import os
os.system("cls")
tabela.append(contato.copy())
print(tabela)

contato['nome'] = "Maria"
contato['idade'] = 20

tabela.append(contato.copy())
print(tabela)
print()

# exibe as keys()
for k in contato.keys():
    print(k)

# exibe os values()
print()
for v in contato.values():
    print(v)

# exibe ambos
print()
for k, v in contato.items():
    print(k, v)

print()
for i in range(len(tabela)):
    print(f"\nNome: {tabela[i]['nome']}")
    print(f"idade: {tabela[i]['idade']}\n")

