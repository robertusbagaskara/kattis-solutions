g, t, n = map(int, input().split())
items = map(int, input().split())
print(int(0.9*(g-t))-sum(items))