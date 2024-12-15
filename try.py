f = open('22.txt')
s = [int(x) for x in f]
mi5 = min(x for x in s if (99 < x < 1000) and x % 10 == 5)
c = 10000005000000000
k = 0
for i in range(len(s)-1):
    for x in range(i + 1, len(s)):
        if ((len(str(s[i])) == 3 and len(str(s[x])) != 3) or (len(str(s[x])) == 3 and len(str(s[i])) != 3)) and ((s[i] + s[x]) % mi5 == 0):
            k += 1
            if s[i] + s[i + 1] < c:
                c = s[i] + s[i + 1]
print(k,c)