N = int(input())
M = int(input())
S = input()

result = 0
i=0
while i<M:
    cnt = 0
    if S[i]=='I':
        i+=1
        while S[i:i+2]=='OI':
            cnt+=1
            i+=2
        if cnt>=N:
            result += cnt-N+1
    else:
        i+=1

print(result)