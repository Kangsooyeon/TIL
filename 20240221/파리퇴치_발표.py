T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    x, y = map(int, input().split())
    li = [list(map(int, input().split())) for _ in range(N)]

    result = 30*15*15+1
    for i in range(N-x+1):
        for j in range(M - y + 1):
            tmp = 0
            for k in range(x):
                for l in range(y):
                    tmp += li[i+k][j+l]

            if tmp%2==0:
                result = min(result, tmp)

    print(f'#{test_case} {result}')