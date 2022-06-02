arr = []
a, b, c, d, e = map(int, input().split())
arr = [a,b,c,d,e]
for i in range(len(arr)):
    for j in range(0,len(arr)-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            dummy = []
            for num in arr:
                dummy.append(str(num))
            print(' '.join(dummy))