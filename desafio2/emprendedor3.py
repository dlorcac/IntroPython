import sys

pventa = float(sys.argv[1])
usuarios = float(sys.argv[2])
gastos = float(sys.argv[3])

if len(sys.argv) < 5:
	ulastyear = 1000
else:
	ulastyear = float(sys.argv[4])

ucurrentyear = pventa * usuarios - gastos
if ucurrentyear > 0:
	ucurrentyear = ucurrentyear - (ucurrentyear * 35 / 100)

percent = ((ucurrentyear / ulastyear) - 1 ) * 100
#percent = (ucurrentyear / ulastyear) * 100

print (int(percent))