'''
number = int(input("Ingrese un número\n"))
if number % 2 != 0:
    for i in range(1, number + 1, 2):
        print(i)
'''
number = int(input("Ingrese un número\n"))
for i in range(1, number + 1):
    if i % 2 != 0:
        print(i)