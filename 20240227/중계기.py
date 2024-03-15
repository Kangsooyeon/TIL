T = int(input())
for tc in range(1, T+1):
    N = int(input())
    li = [list(map(int, input().split())) for _ in range(N+1)]
    R = 0

    for i in range(N+1):
        for j in range(N+1):
            if li[i][j]==2:
                x=i
                y=j

    for i in range(N+1):
        for j in range(N+1):
            if li[i][j]==1:
                hx = i
                hy = j
                D_2 = (hx-x)**2 + (hy-y)**2


                if D_2**0.5 > R:
                    if D_2**0.5==int(D_2**0.5):
                        R = int(D_2**0.5)
                    else:
                        R = int(D_2 ** 0.5) +1

    print(f'#{tc} {R}')