T = int(input())
for tc in range(1,T+1):
    N, Q = map(int, input().split())
    li = [0]*(N+1)

    for i in range(1,Q+1):
        L , R = map(int, input().split())
        for idx in range(L, R+1):
            li[idx] = i

    print('#'+str(tc), *li[1:])