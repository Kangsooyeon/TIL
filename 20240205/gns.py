plan = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

T = int(input())
for tc in range(1,T+1):
    t, N = map(str, input().split())
    li = list(map(str, input().split()))

    print(t)
    num_list =[0]*10

    for l in li:
        num_list[plan.index(l)] +=1

    for i in range(10):
        print((plan[i]+' ')*num_list[i], end='')
    print()