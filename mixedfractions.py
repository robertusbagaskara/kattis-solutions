for x in range(2**31):
    first, second = map(int, input().split())
    if((first==0)and(second==0)):
        break
    else:
        result = first/second
        mod = first%second
        result_out = int(result)
        print('%i %i / %i' % (result_out, mod, second))