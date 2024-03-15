N = int(input())
dp = [0]*(N+1)

for i in range(1,N+1):
    cnt = 0
    for j in range(1,i+1):
        if i%j==0:
            if j>i//j:
                break
            else:
                cnt +=1
    dp[i] = dp[i-1]+cnt

print(dp[N])