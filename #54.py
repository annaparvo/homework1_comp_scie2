from itertools import *
def f(lst, mod):
    output = []
    for value in lst:
        output.append(value**2)
    return sum(output) % mod

if __name__ =='__main__':
    K, M = map(int, raw_input().split())
    lst1 = [list(map(int, raw_input().split()[1:])) for _ in range(K)]
    lst2 = []
    prods = list(product(*lst1))
    for calcs in prods:
        lst2.append(f(calcs,M))
    print max(lst2)