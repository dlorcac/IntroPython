from functools import reduce

auto1 = ['Mazda RX4', 21.0, 6, False, 4]
auto2 = ['Merc 240D', 24.4, 4, True, 2]
auto3 = ['Merc 280', 19.2, 6, True, 4]
auto4 = ['Valiant', 18.1, 6, True, 1]
auto5 = ['Merc 450SL', 17.3, 8, False, 3]
auto6 = ['Toyota Corolla', 33.9, 4, True, 1]

anid_list= [auto1,auto2,auto3,auto4,auto5,auto6] 

anid_list_agrup= [[fila[columna] for fila in anid_list] for columna in range(5)]

media_col_2= reduce(lambda x,y: x + y, anid_list_agrup[1]) / len(anid_list_agrup[1])
media_col_3= reduce(lambda x,y: x + y, anid_list_agrup[2]) / len(anid_list_agrup[2])
media_col_5= reduce(lambda x,y: x + y, anid_list_agrup[4]) / len(anid_list_agrup[4])
print(media_col_5)