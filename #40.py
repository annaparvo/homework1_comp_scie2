a = set(raw_input().split())
print (all(a > set(raw_input().split()) for _ in range(int(input()))))