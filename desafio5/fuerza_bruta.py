word = str(input('Ingrese password: ')).lower()
abc = 'abcdefghijklmnopqrstuvwxyz'
intentos = 0
for i in word:
    for j in abc:
        if i == j:
            intentos += 1
            break
        else:
            intentos += 1
print(intentos, 'Intentos')