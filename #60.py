from collections import deque
if __name__=='__main__':
    d = deque()
    a = int(raw_input())
    for i in range(a):
        f = raw_input().split()
        if f[0] == 'append':
            d.append(int(f[1]))
        if f[0] == 'appendleft':
            d.appendleft(int(f[1]))
        if f[0] == 'pop':
            d.pop()
        if f[0] == 'popleft':
            d.popleft()
    print ' '.join(map(str, d))