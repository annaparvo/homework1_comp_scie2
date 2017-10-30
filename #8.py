if __name__ == '__main__':
    N = int(raw_input())
    list1 = []
    for insert in range(N):
        a = (raw_input()).split()
        if a[0] == 'insert':
            list1.insert(int(a[1]), int(a[2]))
        if a[0] == 'print':
            print list1
        if a[0] == 'remove':
            list1.remove(int(a[1]))
        if a[0] == 'append':
            list1.append(int(a[1]))
        if a[0] == 'sort':
            list1.sort()
        if a[0] == 'pop':
            list1.pop()
        if a[0] == 'reverse':
            list1.reverse()