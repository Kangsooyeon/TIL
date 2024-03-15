T = int(input())
for tc in range(1, T+1):
    N = int(input())
    li = list(map(str, input().split()))

    li_1=[]
    li_2=[]
    result=[]

    for i in range((N+1)//2):
        li_1.append(li[i])
    for i in range((N+1)//2, N):
        li_2.append(li[i])

    while True:
        if li_1:
            result.append(li_1.pop(0))
        if li_2:
            result.append(li_2.pop(0))
        else:
            break
    print(f'#{tc}',*result)