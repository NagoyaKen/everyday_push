A = list(input().split())
if A[0] in 'x':
    if A[1] in '-':
        print(abs(int(A[2]) + int(A[4])))
    else:
        print(abs(int(A[4]) + int(A[2])))
