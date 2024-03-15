def bfs(maze, start, end):
    visited=[[0]*N for _ in range(N)]
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

            if 0<=ni<N and 0<=nj<N and (maze[ni][nj]=='0' or maze[ni][nj]=='3') and visited[ni][nj]==0:
                q.append([ni, nj])
                visited[ni][nj]=1
    return 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    li = [input() for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if li[i][j]=='2':
                start = [i,j]
            elif li[i][j]=='3':
                end = [i,j]

    print(f'#{tc} {bfs(li, start, end)}')