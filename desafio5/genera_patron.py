number = int(input("Ingrese un número\n"))
acumulador = '1\n'
for i in range(2, number + 1):
    for j in range( i ):
        acumulador += str(j + 1)
    acumulador += '\n'
print(acumulador, end = '')