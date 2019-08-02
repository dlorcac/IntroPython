def gen(number):
    abc = 'abcdefghijklmnopqrstuvwxyz'
    acum = ''
    for i in abc:
        acum = acum + i
        if len(acum) == number:
            print(acum)
            
gen (1)