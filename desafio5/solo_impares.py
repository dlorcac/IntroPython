'''
number = int(input("Ingrese un número\n"))
i = 1
if number % 2 != 0:
    for i in range(i,number,2):
            print(i)

    print(number)
'''

number = int(input("Ingrese un número\n"))
if number % 2 != 0:
    for i in range(1, number + 1, 2):
        print(i)