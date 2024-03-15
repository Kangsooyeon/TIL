T = int(input())
for tc in range(1,T+1):
    N = int(input())
    li = [list(map(int, input().split())) for _ in range(N)]
    li = sorted(li, key=lambda x: x[1])
    result = 1
    tmp = li[0][1]

    for i in range(1,N):
        if tmp<=li[i][0]:
            tmp = li[i][1]
            result +=1
        else:
            continue
    print(f'#{tc} {result}')