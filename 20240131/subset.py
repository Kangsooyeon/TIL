N = int(input())
li = list(map(int, input().split()))

for i in range(1<<N): #2^n-1만큼 생성
    for j in range(N):
        if i & (1<<j):
            print(li[j])
    print()
