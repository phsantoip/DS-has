contato = {
    'nome': 'Edson',
    'idade': '50'
}

print(contato)
# nova key
contato['email'] = "eds@hotmail.com"
print(contato)
contato['nome'] = "ester"
print(contato)
contato['Nome'] = "edson"
print(contato)

del contato['Nome']
print(contato)
contato.pop('email')
print(contato)
del contato
