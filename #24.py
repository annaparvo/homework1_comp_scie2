import string
def print_rangoli(size):
    a = string.ascii_lowercase[:size]
    b = a[::-1]
    n = (4*size-3)
    lst1 =[]
    test2 =[]
    for i in range(1,size+1):
        if i <2:
            lst1.append(a[size-1].center(n, '-'))
        else:
            lst1.append(('-'.join(b[0:i]+a[-i+1:])).center(n, '-'))
    test2= lst1[:]
    test2.pop()
    if size == 1:
         print ("a")
    else:
         print ("\n".join(lst1+test2[::-1]))