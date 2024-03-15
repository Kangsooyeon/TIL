def shuffle(li, T):
    if T==0:
        return li

    over_idx = int(N * 0.37)
    tmp = []
    tmp.extend(li[-over_idx:])
    tmp.extend(li[:-over_idx])

    li_1=[]
    li_2=[]
    result=[]

    for i in range((N+1)//2):
        li_1.append(tmp[i])
    for i in range((N+1)//2, N):
        li_2.append(tmp[i])

    while True:
        if li_1:
            result.append(li_1.pop(0))
        if li_2:
            result.append(li_2.pop(0))
        else:
            break
    return shuffle(result, T-1)


TC = int(input())
for tc in range(1,TC+1):
    N, T = map(int, input().split())
    li =[i for i in range(1,N+1)]

    print(f'#{tc}', *shuffle(li,T))