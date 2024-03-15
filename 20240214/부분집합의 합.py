def f(i,k,s,t):
    global cnt
    if s==t:
        tmp=0
        for j in range(k):
            if bit[j]:
                tmp+=1
        if tmp==N:
            cnt+=1
    elif i==k:
        return
    elif s>t:
        return
    else:
        for j in range(1, -1, -1):
            bit[i]=j
            f(i+1, k, s+A[i]*j, t)
    return cnt


T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    A = list(range(1,13))
    bit = [0]*12
    cnt=0
    print(f'#{tc + 1} {f(0,12,0,K)}')