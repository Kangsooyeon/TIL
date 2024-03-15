T= int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    host = list(map(int, input().split()))
    host.sort()

    li = [0]*(host[-1]+1)
    bbang=0
    ans='Possible'

    for i in range(0, len(li)):
        if i==0:
            if i in host:
                ans = 'Impossible'
                break
            else:
                continue

        if i%M==0:
            li[i]=K
            bbang+=K

        if i in host:
            if bbang==0:
                ans = 'Impossible'
                break
            else:
                while i in host and bbang!=0:
                    bbang-=1
                    host.pop(0)

    print(f'#{tc} {ans}')



