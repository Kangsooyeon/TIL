di = [1, -1, 0, 0]
dj = [0, 0, -1, 1]

N= 5
li = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0<=ni<N and 0<=nj<N:
                print(li[ni][nj], end=' ')
        print()