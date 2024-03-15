T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    li = list(map(int, input().split()))

    ans=[]
    for i in range(N-M+1):
        cnt =0
        for j in range(M):
            cnt += li[i+j]
        ans.append((cnt))
    print(f'#{tc} {max(ans) - min(ans)}')