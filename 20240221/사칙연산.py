def post_odrer(v):
    if v:
        post_odrer(left[v])
        post_odrer(right[v])

        if tree[v] in '+-*/':
            a=int(tree[left[v]])
            b=int(tree[right[v]])
            if tree[v] == '+':
                tree[v] = a+b
            elif tree[v] == '-':
                tree[v] = a-b
            elif tree[v] == '*':
                tree[v] = a*b
            elif tree[v] == '/':
                tree[v] = a//b
    return

for tc in range(1,11):
    N = int(input())
    tree = [0]*(N+1)
    left = [0]*(N+1)
    right = [0]*(N+1)

    for _ in range(N):
        s = input().split()
        tree[int(s[0])] = s[1]

        if len(s) == 4:
            left[int(s[0])] = int(s[2])
            right[int(s[0])] = int(s[3])

    post_odrer(1)
    print(f'#{tc} {tree[1]}')