'''
number = int(input("Ingrese un número\n"))
if number % 2 == 0:
    for i in range(0, number + 1, 2):
        print(i)
'''
number = int(input("Ingrese un número\n"))
for i in range(0, number + 1, 2):
    if i % 2 == 0:
        print(i)