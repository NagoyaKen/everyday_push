s = [input() for i in range(2)]
a = int(s[0])
L = []
N = []
num = 0
for i in s[1]:
    num += 1
    if i is 'L':
        L.append(num)
    else:
        N.append(num)
        
L = L[::-1]
L.extend(N)
L = [str(a) for a in L]
L = " ".join(L)

# print('{} and {}'.format(L, N))
