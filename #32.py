n = input()
s = set(map(int, raw_input().split()))
g = int(raw_input())
for i in range(g):
    f = raw_input().split()
    if f[0] == 'discard':
        s.discard(int(f[1]))
    if f[0] == 'remove':
        s.remove(int(f[1]))
    if f[0] == 'pop':
        s.pop()
print sum(s)