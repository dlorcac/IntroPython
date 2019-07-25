#!/usr/bin/python
import sys
import math

gravedad = float(sys.argv[1])
radio = float(sys.argv[2])
radio_mtrs = radio * 1000
total = math.sqrt(2 * gravedad *radio_mtrs)
print (total)
