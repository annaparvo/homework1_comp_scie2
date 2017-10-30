def merge_the_tools(string, k):
    n=len(string)
    for x in xrange(0, n, k):
        slstr = string[x : x+k]
        b =[]
        for y in slstr:
            if y not in b:
                b.append(y)
        print ''.join(b)