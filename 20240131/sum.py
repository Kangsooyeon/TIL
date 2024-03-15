for _ in range(10):
    T = int(input())

    result = 0
    li = []
    for _ in range(100):
        tmp_li = list(map(int, input().split()))
        li.append(tmp_li)
        result = max(result, sum(tmp_li))


    for j in range(100):
        tmp_sum = 0
        for i in range(100):
            tmp_sum += li[i][j]
        result = max(result, tmp_sum)

    diag_left = 0
    diag_right =0
    for i in range(100):
        diag_left += li[i][i]
        diag_right += li[i][99-i]

    result = max(result, diag_left, diag_right)

    print(f'#{T} {result}')