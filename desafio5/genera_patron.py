'''
number = int(input("Ingrese un número\n"))
acumulador = ''
for i in range(number + 1):
    for j in range( i ):
        num_str = str(j + 1)
        acumulador += num_str
    acumulador += '\n'
print(acumulador)
'''

number = int(input("Ingrese un número\n"))
acumulador = ''
for i in range(number + 1):
    for j in range( i ):
        acumulador += str(j + 1)
    acumulador += '\n'
print(acumulador)