A = int(input())
S = []
T = []
for i in range(A):
    S.append(input())
for i in S:
    if i.endswith("s") or i.endswith("sh") or i.endswith("ch") or i.endswith("o") or i.endswith("x"):
      i += 'es'
      T.append(i)
    