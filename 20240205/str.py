T = int(input())
for tc in range(1, T+1):
    N = input()
    M = input()
    if N in M:
        result = 1
    else:
        result =0
    print(f'#{tc} {result}')