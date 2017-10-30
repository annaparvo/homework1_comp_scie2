from itertools import permutations
m,n = raw_input().split()
n = int(n)
m = sorted(list(m))
x = list(permutations(m,n))
for i in x:
    print(''.join(i))