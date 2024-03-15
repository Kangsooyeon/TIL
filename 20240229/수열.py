N, K = map(int, input().split())
li = list(map(int, input().split()))
dp= [0]*(N+1)
tmp = []
for i in range(N):
    dp[i+1]=dp[i]+li[i]

for j in range(K,N+1):
    tmp.append(dp[j]-dp[j-K])

print(max(tmp))