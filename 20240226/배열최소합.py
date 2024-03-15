def func(i,s):
    global result
    if i==N:
        if result>s:
            result = s
    elif s>result:
        return
    else:
        for j in range(i,N):
            P[i], P[j] = P[j], P[i]
            func(i+1, s+li[i][P[i]])
            P[i], P[j] = P[j], P[i]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    li = [list(map(int, input().split())) for _ in range(N)]
    P = [i for i in range(N)]
    result = 1000
    func(0,0)
    print(f'#{tc} {result}')