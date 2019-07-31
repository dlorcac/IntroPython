'''
number = int(input("Ingrese un número\n"))
i = 2
suma = 0
if number % 2 == 0:
    for i in range(i, number, 2):
        suma = suma + i
    suma = suma + number
    print(suma)
'''

number = int(input("Ingrese un número\n"))
if number % 2 == 0:
    sum = 0
    for i in range(2, number + 1, 2):
        sum = sum + i
    print(sum)