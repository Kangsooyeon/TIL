def is_check(board):
    # 가로 확인
    for i in range(N):
        for j in range(N - 4):
            if all(board[i][j + k] == 'o' for k in range(5)):
                return 'YES'
    # 세로 확인
    for i in range(N - 4):
        for j in range(N):
            if all(board[i + k][j] == 'o' for k in range(5)):
                return 'YES'
    # 대각선 확인 (왼쪽 위에서 오른쪽 아래 방향)
    for i in range(N - 4):
        for j in range(N - 4):
            if all(board[i + k][j + k] == 'o' for k in range(5)):
                return 'YES'
    # 대각선 확인 (오른쪽 위에서 왼쪽 아래 방향)
    for i in range(4, N):
        for j in range(N - 4):
            if all(board[i - k][j + k] == 'o' for k in range(5)):
                return 'YES'
    return 'NO'


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    li = [list(map(str, input())) for _ in range(N)]

    print(f'#{tc} {is_check(li)}')