def letra_o(n):
    header = ""
    for i in range(n):
        header += '*'
    center = "*"
    for j in range(n - 2):
        center += " "
    center += "*\n"

    return (header + '\n')  +   (center * (n - 2)) + (header)


n = 10
print(letra_o(n))

'''
    print(header)
    print(center * (n - 2), end = '')
    print(header)
    exit()
'''


