if __name__=='__main__':
    m = raw_input()
    vowels = 'AEIOU'
    s = 0
    k = 0
    for i in range(len(m)):
        if m[i] in vowels:
            k += (len(m)-i)
        else: 
            s += (len(m)-i)
    if k == s:
        print 'Draw'
    if k > s:               
        print 'Kevin', k
    if k < s:
        print 'Stuart', s