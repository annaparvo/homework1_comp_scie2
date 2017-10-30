classlist = []
gradelist = []
lst1 = []
for _ in range(int(raw_input())):
    ppl,grade  = raw_input(),raw_input()
    classlist.append([ppl,grade])
for ppl,grade in classlist:
    gradelist.append(float(grade))
gradelist = list(set(gradelist))
gradelist.sort()
for ppl,grade in classlist:
    if float(grade) == gradelist[1]:
        lst1.append(ppl)
lst1.sort()
print '\n'.join(lst1)