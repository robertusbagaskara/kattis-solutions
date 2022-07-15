if __name__ == '__main__':
    N = int(input())
    if N<100:
        print(99)
    else:
        smaller = int(str(int(N/100)-1)+'99')
        bigger = int(str(int(N/100))+'99')
        if abs(N-bigger) < abs(N-smaller):
            print(bigger)
        elif abs(N-bigger) > abs(N-smaller):
            print(smaller)
        elif abs(N-bigger) == abs(N-smaller):
            print(bigger)