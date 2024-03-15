T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    li = [list(map(int, input().split())) for _ in range(N)]
    K = N+1
    result = 0
    benefit = 0

    for k in range(1, K + 1):
        area = k * k + (k - 1) * (k - 1)  # 운영 영역
        for i in range(N):
            for j in range(N):
                cnt = 0
                for x in range(-(k-1), k):
                    for y in range( -(k-1-abs(x)), k-abs(x)):
                        ni = i+x
                        nj = j+y
                        if 0<=ni<N and 0<=nj<N and li[ni][nj]==1:
                            cnt+=1
                benefit = cnt*M - area #이익
                if 0<=benefit and result < cnt:
                    result = cnt
    print(f'#{tc} {result}')