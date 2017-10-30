from collections import Counter
import sys
if __name__ == "__main__":
    s = raw_input().strip()
    b = (Counter(s).items())
    c = sorted(b, key = lambda x: (-x[1], x[0]))
    for i in range(len(c)):
        if i < 3:
            print c[i][0], c[i][1]