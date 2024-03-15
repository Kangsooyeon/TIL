for tc in range(1, 11):
    n = int(input())
    li = [list(map(int, input().split())) for _ in range(n)]

    result = 0
    for i in range(n):
        flag = 0
        for j in range(n):
            if li[j][i] == 1:
                flag = 1
            elif li[j][i] == 2:
                if flag:
                    result += 1
                    flag = 0

    print(f'#{tc} {result}')