T = int(input())

for tc in range(1,T+1):
    N = float(input())
    ans = 0

    for i in range(13):
        if N >= 2 ** (-i):
            ans +=  10 ** (i - 1)
            N -= 2 ** (-i)
        if N==0:
            break
            
    ans = str(ans)[::-1]

    if N:
        ans = 'overflow'

    print(f'#{tc} {ans}')