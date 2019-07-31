number = int(input("Ingrese un número\n"))
if number % 2 == 0:
    for i in range(0, number + 1, 2):
        print(i)