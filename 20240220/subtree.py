def pre_order(T):
    global cnt
    if T:
        cnt+=1
        pre_order(left[T])
        pre_order((right[T]))
    return cnt

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    li = list(map(int, input().split()))

    left = [0] * (E + 2)
    right = [0] * (E + 2)
    cnt =0

    for i in range(E):
        p, c = li[i * 2], li[i * 2 + 1]

        if left[p] == 0:
            left[p] = c
        else:
            right[p] = c

    print(f'#{tc} {pre_order(N)}')