a, b, c = map(int, input().split())
if a+b==c : print('%i+%i=%i' % (a,b,c))
elif a-b==c : print('%i-%i=%i' % (a,b,c))
elif a*b==c : print('%i*%i=%i' % (a,b,c))
elif a/b==c : print('%i/%i=%i' % (a,b,c))
elif a==b+c : print('%i=%i+%i' % (a,b,c))
elif a==b-c : print('%i=%i-%i' % (a,b,c))
elif a==b*c : print('%i=%i*%i' % (a,b,c))
elif a==b/c : print('%i=%i/%i' % (a,b,c))