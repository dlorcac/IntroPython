import sys

pventa = float(sys.argv[1])
usuarios = float(sys.argv[2])
gastos = float(sys.argv[3])

utilidades = pventa * usuarios - gastos
if utilidades > 0:
	resultado = utilidades - (utilidades * 35 / 100)
	print(resultado)
else:
  print(utilidades)