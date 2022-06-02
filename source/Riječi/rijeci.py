k = int(input())
A = []
B = []
A.append(0)
A.append(1)
B.append(1)
B.append(1)
if(k>=3):
    for i in range(2, k):
        A.append(A[i-1] + A[i-2])
        B.append(B[i-1] + B[i-2])
print('%i %i' % (A[k-1], B[k-1]))