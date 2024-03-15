for _ in range(10):
    T = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for i in range(100):
        x= i
        y = 0
        if ladder[y][x]==0:
            continue

        while y<99:
            y = y + dy[1]

            if ladder[y][x] == 2:
                break

            if x!=0 and ladder[y][x+dx[2]] ==1:
                while x!=0 and ladder[y][x+dx[2]]==1:
                    x = x+dx[2]

            elif x!=99 and ladder[y][x+dx[3]] ==1:
                while x!=99 and ladder[y][x+dx[3]]==1:
                    x = x+dx[3]

        if ladder[y][x] == 2:
            print(f'#{T} {i}')
            break