N = int(input())
a = []
d = 0
for i in range(N):
   a.append(input().split())

for i in a:
    if i[0] =='s':
        i.pop(0)
        i = [int(_) for _ in i] 
        b = sum(i)
        c = i[1] + i[2]
        if b >= 350 and c >= 160:
            d += 1
            
        
    else:
        i.pop(0)
        i = [int(_) for _ in i] 
        b = sum(i)
        c = i[3] + i[4]
        if b >= 350 and c >= 160:
            d += 1
