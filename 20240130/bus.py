T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    li = [0]*5001

    for _ in range(N):
        a, b = map(int, input().split())
        for i in range(a,b+1):
            li[i] +=1

    P = int(input())
    result = []
    for _ in range(P):
        result.append(li[int(input())])

    print('#'+str(test_case), *result)