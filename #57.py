from collections import *
from collections import namedtuple
if __name__=='__main__':
    a = int(raw_input())
    b = namedtuple('b', raw_input())
    j = []
    for _ in range(a):
        info = raw_input().split()
        j+= (float(s.MARKS) for s in [b(*info)])
    print '{0:.2f}'.format(sum(j)/a)