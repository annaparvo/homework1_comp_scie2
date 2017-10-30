from itertools import combinations_with_replacement
m,n = raw_input().split()
n = int(n)
m = sorted(list(m))
x = list(combinations_with_replacement(m,n))
for i in x:
    print(''.join(i))