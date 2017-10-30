import cmath
import math
a = raw_input()
b = cmath.phase(complex(a))
c = abs(complex(a))

print ("{0}\n{1}".format(c,b))