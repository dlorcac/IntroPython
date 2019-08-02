'''
def letra_x(size):
    for i in range(0,size, 1):
        for j in range(0,size,1):
            if i==j or j==(size -i -1):
                print("*")
            else:
                print(" ")
        #print("\n")

letra_x(11)

'''

def letra_x(size):
    i,j = 0,size - 1
    acum=''
    while j >= 0 and i < size:

        initial_spaces = ' '*min(i,j)
        middle_spaces = ' '*(abs(i - j) - 1)
        final_spaces = ' '*(size - 1 - max(i,j))

        if j == i:
            #print (initial_spaces + '*' + final_spaces)
            acum += initial_spaces + '*' + final_spaces + '\n'
        else:
            #print (initial_spaces + '*' + middle_spaces + '*' + final_spaces)
            acum +=initial_spaces + '*' + middle_spaces + '*' + final_spaces + '\n'

        i += 1
        j -= 1
    return acum

#print (letra_x(11))
letra_x(11)
