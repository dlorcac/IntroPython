number = int(input("Ingrese un número\n"))
i = 2
suma = 0
if number % 2 == 0:
    for i in range(i, number, 2):
        suma = suma + i
    suma = suma + number
    print(suma)