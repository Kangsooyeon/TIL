T = int(input())
for tc in range(1, T+1):
    N = int(input())
    li = [list(map(int, input().split())) for _ in range(N)]
    size = 1
    ans=0
    tmp =0

    for i in range(N):
        for j in range(N):
            for k in range(i+tmp,N):
                for l in range(j+tmp,N):
                    if li[i][j]==li[k][l]:
                        size_tmp = (k-i+1) * (l-j+1)
                        if size_tmp==size:
                            ans+=1
                        elif size_tmp>size:
                            tmp = min(k-i, l-j)
                            size = size_tmp
                            ans = 0
                            ans+=1

    print(f'#{tc} {ans}')