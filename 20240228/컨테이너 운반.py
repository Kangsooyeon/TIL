T =int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    nw = list(map(int, input().split()))
    mt = list(map(int, input().split()))
    nw.sort(reverse=True)
    mt.sort(reverse=True)

    result = 0

    for i in range(N):
        for j in range(M):
            if nw[i]!=0 and mt[j]!=0 and nw[i]<=mt[j]:
                result += nw[i]
                nw[i]=0
                mt[j]=0

    print(f'#{tc} {result}')