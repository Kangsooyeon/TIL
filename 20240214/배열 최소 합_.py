def f(i, k, s):
    global  min_v
    if i==k:
        if min_v>s:
            min_v=s
    elif s>=min_v:
        return
    else:
        for j in range(i, k):
            P[i], P[j] = P[j], P[i]
            f(i+1, k, s+li[i][P[i]])
            P[i], P[j] = P[j], P[i]

T = int(input())
for tc in range(1,T+1):
    N=int(input())
    li=[list(map(int, input().split())) for _ in range(N)]
    P=[i for i in range(N)]
    min_v=100
    f(0, N, 0)
    print(f'#{tc} {min_v}')