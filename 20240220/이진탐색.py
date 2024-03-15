def in_order(T):
    if T<N+1:
        in_order(T*2)
        ans.append(T)
        in_order(T*2+1)
    return ans

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    li = list(range(0,N+1))
    ans=[0]
    in_order(1)
    print(f'#{tc} {ans.index(1)} {ans.index(N//2)}')