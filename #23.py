def print_formatted(number):
    a = len(bin(number)[2:])
    for i in range(1, number+1):
        oc = oct(i)[1:]
        he = (hex(i)[2:]).upper()
        bi = bin(i)[2:]
        print "{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, oc, he, bi, width=a)