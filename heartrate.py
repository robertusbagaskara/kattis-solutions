N = int(input())
for i in range(N):
    b, p = map(float, input().split())
    BPM = 60*b/p 
    APBM = 60/p 
    print('%.4f %.4f %.4f' % (BPM-APBM, BPM, BPM+APBM))