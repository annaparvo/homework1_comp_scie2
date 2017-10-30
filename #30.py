if __name__ == '__main__':
    m = raw_input()
    arr = list(raw_input().split())
    a = set(raw_input().split())
    b = set(raw_input().split())
    happy = 0
    for i in arr:
        if i in a:
            happy += 1
        if i in b:
            happy -= 1
    print happy