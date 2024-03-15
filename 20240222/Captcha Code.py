T = int(input())
for tc in range(1,T+1):
    N, K = map(int, input().split())
    sample = list(map(int, input().split()))
    passcode = list(map(int, input().split()))

    s_idx=0
    p_idx=0

    while s_idx<N and p_idx<K:
        if passcode[p_idx]==sample[s_idx]:
            p_idx+=1
            s_idx+=1

        else:
            s_idx+=1

    if p_idx==K:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')
