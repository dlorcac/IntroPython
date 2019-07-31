'''
number = int(input("Ingrese un número\n"))
i = 0
for i in range(i, number, 2):
    if number % 2 == 0:
        print(i + 2)
    else:
        exit()
'''

number = int(input("Ingrese un número\n"))
if number % 2 == 0:
    for i in range(2, number + 1, 2):
        print(i)