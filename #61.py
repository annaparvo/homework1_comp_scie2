from collections import deque
if __name__=='__main__':
    for _ in range(int(raw_input())):
        a = int(raw_input())
        b = deque(map(int, raw_input().split()))
        for i in range(a-1):
            if b[0] >= b[1]:
                b.popleft()
            elif b[-1] >= b[-2]:
                b.pop()
        if len(b) > 1:
            print 'No'
        else:
            print 'Yes'