def bfs(s,N):
    q = []
    visited = [0]*(N+1)
    q.append(s)
    visited[s] = 1
    while q:
        t=q.pop(0)
        for i in adjl[t]:
            if visited[i]==0:
                q.append(i)
                visited[i] = 1 + visited[t]

    for m in range(100,0,-1):
        if visited[m]==max(visited):
            return m


for tc in range(1,11):
    N, start = map(int, input().split())
    li = list(map(int, input().split()))


    adjl = [[] for _ in range(101)]
    for i in range(N//2):
        n1, n2 = li[i * 2], li[i * 2 + 1]
        adjl[n1].append(n2)

    print(f'#{tc} {bfs(start, 100)}')