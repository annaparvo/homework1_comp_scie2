from itertools import combinations
a, b, c = int(raw_input()), raw_input().split(), int(raw_input())
x = list(combinations(b,c))
a1 = 0
for i in x:
    if 'a' in i:
        a1 += 1
print float(a1)/float(len(x))