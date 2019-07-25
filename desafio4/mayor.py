import sys

numeros = sys.argv[1 :]
mayor = max(numeros, key=int)
print(mayor)