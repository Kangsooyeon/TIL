T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())

    adjl = [[] for _ in range(V+1)]
    for i in range(E):
        n1, n2 = map(int, input().split())
        adjl[n1].append(n2)

    s, g = map(int, input().split())

    visited = [0] * (V + 1)
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

    print(f'#{tc} {visited[g]}')