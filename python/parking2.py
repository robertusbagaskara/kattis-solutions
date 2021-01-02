t = int(input())

for i in range(t):
    n = int(input())
    stores = input().split()
    for k in range(n):
        stores[k] = int(stores[k])
    stores.sort()
    print((max(stores) - min(stores)) * 2)