from itertools import combinations
m,n = raw_input().split()
n = int(n)
m = sorted(list(m))
for i in range(1, n+1):
    x = list(combinations(m,i))
    x.sort()
    for i in x:
        print(''.join(i))