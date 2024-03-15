N = int(input())
P = list(map(int, input().split()))
num = 0
P.sort()
for i in range(N):
    for j in range(i + 1):
        num += P[j]
print(num)