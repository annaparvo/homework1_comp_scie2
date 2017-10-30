input()
set1 = set(raw_input().split())
gn = int(raw_input())
for i in range(gn):
    eval('set1.{0}({1})'.format(raw_input().split()[0], raw_input().split()))
print(sum(map(int, set1)))