T = int(input())

for tc in range(1, T + 1):

    K, N, M = map(int, input().split())
    li = list(map(int, input().split()))

    cnt = 0
    i = 0

    while i + K < N:
        for j in range(K, 0, -1):
            if i + j in li:
                i += j
                cnt += 1
                break
        else:
            cnt = 0
            break

    print(f'#{tc} {cnt}')