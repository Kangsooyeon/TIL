for _ in range(10):
    T, E = map(int, input().split())
    li = list(map(int, input().split()))

    adjl = [[] for _ in range(100)]

    for i in range(E):
        n1, n2 = li[i*2], li[i*2+1]
        adjl[n1].append(n2)

    s=0
    visited = [0] * 100
    stack = []
    visited[s] = 1
    while True:
        for w in adjl[s]:
            if visited[w] == 0:
                stack.append(s)
                s = w
                visited[s] = 1
                break
        else:
            if stack:
                s = stack.pop()
            else:
                break
    print(f'#{T} {visited[99]}')