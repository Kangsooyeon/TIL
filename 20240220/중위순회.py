def in_order(T):
    if T:
        in_order(left[T])
        ans.append(li[T-1][1])
        in_order(right[T])
    return ans

for tc in range(1,11):
    N = int(input())
    li = [list(map(str, input().split())) for _ in range(N)]
    left = [0]*(N+1)
    right = [0] * (N + 1)
    ans = []

    for i in range(N):
        if len(li[i])>=3:
            left[i+1] = int(li[i][2])
            if len(li[i])==4:
                right[i+1]=int(li[i][3])

    print(f'#{tc}', ''.join(in_order(1)))

    # def inorder(p):
    #     if p <= N:
    #         inorder(p*2)
    #         print(tree[p],end ="")
    #         inorder(p*2+1)
    #
    # for t in range(10):
    #     N = int(input())
    #     lst = []
    #     tree = [0] * (N + 1)
    #     for _ in range(N):
    #         lst = list(map(str,input().split()))
    #         tree[int(lst[0])] = lst[1]
    #     # print(tree)
    #     print(f'#{t+1}',end ="")
    #     inorder(1)
    #     print()