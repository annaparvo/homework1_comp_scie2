import collections
from collections import Counter
if __name__=='__main__':
    numShoes = int(raw_input())
    shoes = collections.Counter(map(int, raw_input().split()))
    c = int(raw_input())
    d = 0
    for i in range(c):
        s, p = map(int, raw_input().split())
        if shoes[s]:
            d += p
            shoes[s] -= 1
    print d