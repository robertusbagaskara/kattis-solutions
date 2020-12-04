l, r = map(int, input().split())
output = 0
if l+r==0:
    print('Not a moose')
elif l==r:
    print('Even %i' % (l+r))
elif l!=r:
    if l>r:
        output = l*2
    elif r>l:
        output = r*2
    print('Odd %i' % (output))