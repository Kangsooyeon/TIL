T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    li = input()

    result = 0
    cnt = 0

    for i in li:
        if i == '1':
            cnt+=1
            result = max(result, cnt)
        else:
            cnt = 0

    print(f'#{test_case} {result}')