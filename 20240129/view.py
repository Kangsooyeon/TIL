for test_case in range(1, 11):
    N = int(input())
    li = list(map(int, input().split()))
    result=0

    for i in range(2,N-2):
        if li[i]==0:
            continue
        else:
            new_li=[]
            for j in range(i-2, i+3):
                new_li.append(li[j])

            tmp_max = max(new_li)
            if tmp_max == li[i]:
                new_li.remove(tmp_max)
                second_max = max(new_li)
                result += tmp_max - second_max

    print(f'#{test_case} {result}')


