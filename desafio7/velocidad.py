def promedio(velocidad):
    suma=0
    for value in enumerate(velocidad):
        suma = suma + value[1]
    return (suma/len(velocidad))



velocidad = [4, 4, 7, 7, 8, 9, 10, 10, 10,
            11, 11, 12, 12, 12, 12, 13, 13,
            13, 13, 14, 14, 14, 14, 15, 15,
            15, 16, 16, 17, 17, 17, 18, 18,
            18, 18, 19, 19, 19, 20, 20, 20,
            20, 20, 22, 23, 24, 24, 24, 24, 25]

pepe=promedio(velocidad)
print(pepe)