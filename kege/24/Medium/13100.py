s = open("24.txt").readline()

k1 = k2 = c1 = c2 = m = 0

for x in range(len(s)):
    if s[x] == 'C': k1 += 1
    if s[x] == 'D': k2 += 1
    while k1 > 2:
        if s[c1] == 'C': k1 -= 1
        c1 += 1
    while k2 > 2:
        if s[c2] == 'D': k2 -= 1
        c2 += 1
    C = max(c1,c2)
    m = max(m,x-C+1)

print(m)
