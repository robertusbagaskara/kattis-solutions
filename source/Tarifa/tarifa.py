x = int(input())
n = int(input())
megabytes = x
for i in range(n):
    spent = int(input())
    megabytes -= spent
    megabytes += x
print(megabytes)
