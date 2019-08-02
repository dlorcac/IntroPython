import math

def letra_i(n):
    header = ""
    for i in range(n):
        header += '*'
    center = ""
    mitad = math.ceil(n/2)
    for j in range(1,n):
        if j == mitad:
            center += "*"
        else:
            center += " "
    center += "\n"
    print(center)
    return (header + '\n') + (center * (n - 2)) + (header)

n = 10
print(letra_i(n))

'''
    print(header)
    print(center * (n - 2), end = '')
    print(header)
    exit()
'''


