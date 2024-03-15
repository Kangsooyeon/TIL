def fact(k):
    ans = 1
    for i in range(1, k+1):
        ans *= i
    return ans

def nCr(n, r):
    return fact(n) // (fact(r) * fact(n-r))

T = int(input())
for tc in range(1, T+1):
    N =int(input())
    print(f'#{tc}')
    for i in range(N):
        for j in range(i+1):
            print(nCr(i, j), end=' ')
        print()