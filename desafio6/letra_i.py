def letra_i(n):
    contain_bounds = ""
    for i in range(n):
        contain_bounds += '*'
    contain_middle = "  *"
    for j in range(n - 2):
        contain_middle += "   "
    contain_middle += "\n"


    print(contain_bounds)
    print(contain_middle * (n - 2), end = '')
    print(contain_bounds)
    exit()

#n = 5
print(letra_i(5))
