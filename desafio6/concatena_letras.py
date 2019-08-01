def gen(number):
    abc = 'abcdefghijklmnopqrstuvwxyz'
    acum = ''
    p = 0
    while p < number:
        for i in abc(number):
            acum = acum + i
        p += 1
        print(acum)
            
gen (4)