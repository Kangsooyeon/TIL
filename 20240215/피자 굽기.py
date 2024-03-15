T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    chz = list(map(int, input().split()))

    idx = list(range(1,M+1))
    Q_c=[]
    Q_i=[]

    for _ in range(N):
        Q_c.append(chz.pop(0))
        Q_i.append((idx.pop(0)))

    while len(Q_c)!=1:
        tmp_c=Q_c.pop(0)
        tmp_i=Q_i.pop(0)
        if tmp_c!=1:
            Q_c.append(tmp_c//2)
            Q_i.append(tmp_i)
        else:
            if chz:
                Q_c.append(chz.pop(0))
                Q_i.append((idx.pop(0)))

    print(f'#{tc}', *Q_i)
