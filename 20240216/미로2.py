def bfs(maze, start, end):
    visited=[[0]*100 for _ in range(100)]
    q =[]

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    q.append(start)
    visited[start[0]][start[1]]=1

    while q:
        tmp = q.pop(0)

        if tmp==end:
            return 1

        i, j = tmp

        for k in range(4):
            ni = i+di[k]
            nj = j+dj[k]

            if 0<=ni<100 and 0<=nj<100 and (maze[ni][nj]==0 or maze[ni][nj]==3) and visited[ni][nj]==0:
                q.append([ni, nj])
                visited[ni][nj]=1
    return 0

for _ in range(10):
    T = int(input())
    li = [list(map(int, input())) for _ in range(100)]

    for i in range(100):
        for j in range(100):
            if li[i][j]==2:
                start = [i,j]
            elif li[i][j]==3:
                end = [i,j]

    print(f'#{T} {bfs(li, start, end)}')