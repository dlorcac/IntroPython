import sys

pventa = float(sys.argv[1])
usuariost = float(sys.argv[2])
usuariosp = float(sys.argv[3])
usuariosg = float(sys.argv[4])
gastos = float(sys.argv[5])

#if (usuariosp + usuariosg) != usuariost:
#	print("La suma de usuarios premium + gratuitos no coincide con el total de usuarios.")
#	sys.exit()

utilidades = pventa * (usuariosp * 2) - gastos
if utilidades > 0:
	utilidades = utilidades - (utilidades * 35 / 100)
	print(utilidades)
else:
  print(utilidades)