T = int(input())
for tc in range(1, T+1):
    N =int(input())
    li = [[0]*N for _ in range(N)]

    li[0][0] = 1

    for i in range(1,N):
        li[i][0] = 1
        li[i][i] = 1
        for j in range(1,i):
            li[i][j] = li[i-1][j-1] + li[i-1][j]

    print(f'#{tc}')
    for k in range(len(li)):
        print(*li[k][:k+1])