def f(i, k):
    global  min_v
    global  cnt
    cnt+=1
    if i==k:
        #print(*P)
        s=0     #선택한 원소의 합
        for j in range(k):      #j행에 대해
            s+=li[j][P[j]]      #j행에서 P[j]열을 고른 경우의 합 구하기
        if min_v>s:
            min_v=s
    else:
        for j in range(i, k):   #P[i]자리에 올 원소 P[j]
            P[i], P[j] = P[j], P[i]     #P[i] <-> P[j]
            f(i+1, k)
            P[i], P[j] = P[j], P[i]  # 교환 전으로 복구

N=int(input())
li=[list(map(int, input().split())) for _ in range(N)]
P=[i for i in range(N)]
min_v=100
cnt =0
f(0, 3)
print(min_v, cnt)
