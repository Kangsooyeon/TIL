for tc in range(1,11):
    N = int(input())
    li = [list(map(str, input())) for _ in range(8)]

    cnt =0

    for i in range(8):
        for j in range(8-N+1):
            tmp =''.join(li[i][j:j + N])
            if tmp==tmp[::-1]:
                cnt +=1

    for j in range(8):
        for i in range(8 - N + 1):
            tmp = ''.join(li[i + k][j] for k in range(N))
            if tmp == tmp[::-1]:
                cnt += 1

    print(f'#{tc} {cnt}')