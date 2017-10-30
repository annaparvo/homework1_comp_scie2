from collections import OrderedDict
if __name__=='__main__':
    a = int(raw_input())
    c = OrderedDict()
    for i in range(a):
        b,_,p = raw_input().rpartition(' ')
        if b in c:
            c[b] += int(p)
        else:
            c[b] = int(p)
    for b, p in c.items():
        print b, p