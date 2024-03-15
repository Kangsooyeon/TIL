di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T+1):
    N, P = map(int, input().split())
    li = [list(map(int, input().split())) for _ in range(N)]
    ans = 0

    for i in range(N):
        for j in range(N):
            cnt = li[i][j]
            for k in range(4):
                for l in range(1,P+1):
                    ni = i + di[k]*l
                    nj = j + dj[k]*l

                    if 0<=ni<N and 0<=nj<N:
                        cnt +=li[ni][nj]

            ans = max(ans, cnt)

    print(f'#{tc} {ans}')