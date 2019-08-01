'''
number = int(input("Ingrese un número\n"))
if number % 2 == 0:
    sum = 0
    for i in range(2, number + 1, 2):
        sum = sum + i
    print(sum)
'''
number = int(input("Ingrese un número\n"))
suma = 0
for i in range(0, number + 1, 2):
    if i % 2 == 0:
        suma = suma + i
print(suma)