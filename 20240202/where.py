T = int(input())
for test_case in range(1, T+1):
    N, K  = map(int, input().split())
    li = [list(map(int, input().split())) +[0] for _ in range(N)] + [[0]*(N+1)]
    N+=1

    ans = 0
    for i in range(N):
        cnt = 0
        for j in range(N):
            if li[i][j]:
                cnt +=1

            else:
                if cnt ==K:
                    ans +=1
                cnt =0

    for j in range(N):
        cnt = 0
        for i in range(N):
            if li[i][j]:
                cnt +=1

            else:
                if cnt ==K:
                    ans +=1
                cnt =0


    print(f'#{test_case} {ans}')