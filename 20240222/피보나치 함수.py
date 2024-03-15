T = int(input())
for _ in range(T):
    N = int(input())
    f0=[0]*41
    f1=[0]*41

    f0[0]=1
    f1[1]=1

    for i in range(2,41):
        f0[i]=f0[i-1]+f0[i-2]
        f1[i]=f1[i-1]+f1[i-2]
    print(f0[N], f1[N])
