N = int(input())
li = [int(input()) for _ in range(N)]
li.sort(reverse=True)

ans = li[0]
for i in range(1,N):
    ans = max(li[i]*(i+1), ans)

print(ans)