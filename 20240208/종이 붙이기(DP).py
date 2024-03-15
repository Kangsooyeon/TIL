T = int(input())
for tc in range(1,T+1):
    N = int(input())//10
    d=[0]*(N+1)

    d[1]=1
    d[2]=3

    for i in range(3, N+1):
        d[i] = d[i-1] + d[i-2]*2

    print(f'#{tc} {d[N]}')