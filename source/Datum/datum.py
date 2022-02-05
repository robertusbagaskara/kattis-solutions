import datetime
day, month = map(int, input().split())
x = datetime.datetime(2009, month, day)
print(x.strftime('%A'))