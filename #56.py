import collections
from collections import defaultdict
if __name__=='__main__':
    n,m=map(int, raw_input().split())
    a = defaultdict(list)
    for i in range(n):
        a[raw_input()].append(str(i+1))
    for i in range(m):
        print(' '.join(a[raw_input()]) or -1)