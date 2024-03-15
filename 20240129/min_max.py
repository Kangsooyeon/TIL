T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    li = list(map(int, input().split()))

    result = max(li)-min(li)
    print(f'#{test_case} {result}')