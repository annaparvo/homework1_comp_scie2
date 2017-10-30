def capitalize(string):
    a = list(string)
    a[0]= a[0].upper()
    for x in range(len(a)):
        if a[x] == ' ':
            a[x+1]=a[x+1].upper()
    return ''.join(a)