def letra_x(size):
    diag_a = ''
    for i in range(0, size):
        if i ==
        else:
        diag_a+=
        diag_a=

print (letra_x(11))

''' 
def letra_x(size):
    i,j = 0,size - 1

    while j >= 0 and i < size:

        initial_spaces = ' '*min(i,j)
        middle_spaces = ' '*(abs(i - j) - 1)
        final_spaces = ' '*(size - 1 - max(i,j))

        if j == i:
            print (initial_spaces + '*' + final_spaces)
        else:
            print (initial_spaces + '*' + middle_spaces + '*' + final_spaces)

        i += 1
        j -= 1

print (letra_x(11))
'''

