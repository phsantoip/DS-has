notas = {
    'Edson': 10,
    'Marion': 10,
    'Luana': 3
}
import os
os.system("cls")

print(notas)

del notas['Edson']
notas.pop('Edson')
# notas.clear()
print(notas)