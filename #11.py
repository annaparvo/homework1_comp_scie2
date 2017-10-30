if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    arr.sort()
    a = arr[n-1]
    while a == arr[-1]:
        arr.pop()
    b = max(arr)
    print b