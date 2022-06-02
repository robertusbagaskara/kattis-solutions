result = []
for i in range(5):
    a, b, c, d = map(int, input().split())
    sum = a+b+c+d
    result.append(sum)  
for i in range(5):
    if(result[i] == max(result)):
        index = i 
print(index+1, max(result))

    