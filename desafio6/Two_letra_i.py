import math
def qa(n):
    header = ''
    for i in range(n):
        header +='*'
    #header += '\n'
#    print(header)
    center = ''
    mitad = int(math.ceil(n/2))
    print(mitad)
    for j in range(1, n + 1 ): 
        if j == mitad:
            center += '*'
        else:
            center += ' '
    center = (center + '\n') * (n - 2)
    print(header)
    print(center, end='')
    print(header)

n = 8
print(qa(n), end=' ')