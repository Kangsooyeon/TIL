T = int(input())
for test_case in range(T):
    N, K = map(int, input().split())
    li = []
    for _ in range(N):
        li.append(list(map(int, input().split())))

    print(li)