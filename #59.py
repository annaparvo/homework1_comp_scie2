from collections import OrderedDict
a = int(raw_input())
dic = OrderedDict()
for i in range(a):
    words = raw_input()
    dic.setdefault(words, 0)
    dic[words] += 1
print len(dic)
print " ".join(str(i) for i in dic.values())