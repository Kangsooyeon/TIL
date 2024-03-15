T = int(input())
for tc in range(1, T+1):
    N = int(input())
    li = [list(map(int, input().split())) for _ in range(N)]

    #재귀?
    #되돌아가서 다시 탐색

    col =[]
    result = []
    for i in range(N):
        for j in range(N): #while로?
            if j not in col:
                col.append(j)
                result.append(li[i][j])
                break
    print(col)
    print(result)