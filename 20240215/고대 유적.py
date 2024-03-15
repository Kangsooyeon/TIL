di = [0, 1] #우하
dj = [1, 0]

T = int(input())
for tc in range(1, T+1):
    N,M = map(int, input().split())
    li = [list(map(int, input().split())) for _ in range(N)]

    ans=0
    for i in range(N):
        for j in range(M):
            if li[i][j]==1:
                for k in range(2):
                    l=1
                    while 0<=i+di[k]*l<N and 0<=j+dj[k]*l<M and li[i+di[k]*l][j+dj[k]*l]==1:
                        l+=1
                    ans=max(ans, l)

    print(f'#{tc} {ans}')