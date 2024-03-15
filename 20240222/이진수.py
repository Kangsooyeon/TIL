T = int(input())
for tc in range(1, T+1):
    N, S = map(str, input().split())
    result =''
    for i in range(int(N)):
        result += bin(int('0x' + S[i], 16))[2:].zfill(4)
    print(f'#{tc} {result}')
