T = int(input())

for tc in range(T):
    N, K = map(int, input().split())
    li = list(range(1, 13))
    cnt = 0

    for i in range(1 << 12):
        subset = [li[j] for j in range(12) if (i & (1 << j)) > 0]
        if len(subset) == N and sum(subset) == K:
            cnt += 1

    print(f'#{tc+1} {cnt}')