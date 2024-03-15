T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    li = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    for i in range(N-M+1):
        for j in range(N - M + 1):
            tmp = 0
            for x in range(M):
                for y in range(M):
                    tmp += li[i+x][j+y]

            result = max(result, tmp)

    print(f'#{test_case} {result}')