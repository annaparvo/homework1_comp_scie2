import math
ab = int(raw_input())
bc = int(raw_input())
f = int(round(math.degrees(math.atan2(ab,bc))))
print str(f)+'°'