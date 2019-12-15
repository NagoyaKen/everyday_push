a,b = map(int,input().split())
c = list(map(int, input().split())) 
 
print(len([i for i, x in enumerate(c) if x>=b]))
