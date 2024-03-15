T = int(input())
for tc in range(1, T+1):
    N = int(input())
    li_a = []
    li_b = []
    for _ in range(N):
        A, B = map(int, input().split())
        li_a.append(A)
        li_b.append(B)

    result = 0
    for i in range(1,N):
        for j in range(i):
            if li_a[j]<li_a[i] and li_b[j]>li_b[i]:
                result+=1
            elif li_a[j]>li_a[i] and li_b[j]<li_b[i]:
                result+=1
    print(f'#{tc} {result}')