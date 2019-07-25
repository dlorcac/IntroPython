import sys
import random

user = sys.argv[1]
option = ['piedra', 'papel', 'tijera']
machine = random.choice(option)
if user not in option:
  print("Argumento inválido: Debe ser piedra, papel o tijera.")
  exit()

print("Computador juega {}".format(machine))
if (user == 'piedra'):
  if (machine == 'tijera'):
    print("Ganaste")
  elif (machine == 'piedra'):
    print("Empataste")
  elif (machine == 'papel'):
    print("Perdiste")

if (user == 'tijera'):
  if (machine == 'papel'):
    print("Ganaste")
  elif (machine == 'tijera'):
    print("Empataste")
  elif (machine == 'piedra'):
    print("Perdiste")

if (user == 'papel'):
  if (machine == 'piedra'):
    print("Ganaste")
  elif (machine == 'papel'):
    print("Empataste")
  elif (machine == 'tijera'):
    print("Perdiste")