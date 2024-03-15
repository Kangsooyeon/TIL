def bfs(s,N):   #시작정점 s, 노드개수 N
    q = []                  # 큐
    visited = [0]*(N+1)     # visited
    q.append(s)             # 시작점 인큐
    visited[s] = 1          # 시작점 방문표시
    while q:                # 큐가 비워질때까지...(남은 정점이 있으면)
        t=q.pop(0)
        # t에서 할일...
        print(t)
        for i in adjl[t]:   # t에 인접인 정점 i
            if visited[i]==0:   #방문하지 않은 정점이면
                q.append(i)     #인큐
                visited[i] = 1 + visited[t]     #방문표시
    print(visited)


V, E = map(int, input().split())
arr = list(map(int, input().split()))

adjl =[[] for _ in range(V+1)]
for i in range(E):
    n1, n2 = arr[i*2], arr[i*2+1]
    adjl[n1].append(n2)
    adjl[n2].append(n1)

bfs(1,V)