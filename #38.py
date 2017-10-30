a = int(input())
b = raw_input().split()
set1 = set()
set2 = set()
for i in b:
    if i in set1:
        set2.add(i)
    else:
        set1.add(i)
s = set1.difference(set2)
print list(s) [0]