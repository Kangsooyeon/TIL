T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    info_li = [list(map(int, input().split())) for _ in range(N)]
    li = [[0]*10 for _ in range(10)]

    for info in info_li:
        if info[-1]==1:
            for i in range(info[0],info[2]+1):
                for j in range(info[1], info[3]+1):
                    li[i][j] = 1

    for info in info_li:
        if info[-1]==2:
            for i in range(info[0],info[2]+1):
                for j in range(info[1], info[3]+1):
                    if li[i][j] != 2:
                        li[i][j] +=2

    result =0
    for l in li:
        result += l.count(3)

    print(f'#{test_case} {result}')