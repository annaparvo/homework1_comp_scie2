from itertools import product
a = map(int, raw_input().split())
b = map(int, raw_input().split())
c = list(product(a, b))
print ' '.join(map(str,c))