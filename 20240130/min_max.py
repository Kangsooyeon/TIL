T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    li = list(map(int, input().split()))

    max_id_li = list(filter(lambda x: li[x] == max(li), range(N)))
    max_id = max(max_id_li)
    min_id = li.index(min(li))

    result = abs(max_id - min_id)
    print(f'#{test_case} {result}')