T = int(input())
di = [-1, 1, 0, 0] #상하좌우
dj = [0, 0, -1, 1]
for tc in range(1, T+1):
    N = int(input())
    li = [list(map(int, input())) for _ in range(N)]
    check= [[0]*N for _ in range(N)]
    stack = []
    ans = 0

    def dfs(i,j):
        if li[i][j]==3:
            return 1

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]

            if ni<0 or ni>=N or nj<0 or nj>=N or li[ni][nj]==1:
                continue
            if li[ni][nj]==0 and check[ni][nj]==0:
                check[ni][nj]=1
                return dfs(ni, nj)










    print(stack)

