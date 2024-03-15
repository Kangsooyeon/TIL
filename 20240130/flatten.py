for test_case in range(1,11):
    N = int(input())
    li = list(map(int, input().split()))

    result = max(li) - min(li)

    for _ in range(N):
        if result==0 or result==1:
            break
        else:
            max_id = li.index(max(li))
            min_id = li.index(min(li))

            li[max_id] -=1
            li[min_id] +=1

            result = max(li) - min(li)

    print(f'#{test_case} {result}')