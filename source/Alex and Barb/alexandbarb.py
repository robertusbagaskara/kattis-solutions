k, m, n = map(int, input().split())
print("Barb" if (k%(m+n)<m) else "Alex")