def switching(idx): #1->0 , 0->1
    switch[idx] = 1-switch[idx]

N = int(input())
switch = list(map(int, input().split()))
S = int(input())

for _ in range(S):
    gender, num = map(int, input().split())

    if gender==1:
        for n in range(1,N//num+1):
            switching(num*n-1)

    elif gender==2:
        switching(num - 1)
        k = 1
        while 0<=num-1-k and num-1+k<N and switch[num-1-k]==switch[num-1+k]:
            switching(num-1-k)
            switching(num-1+k)
            k+=1

for i in range(0,N,20):
    print(*switch[i:i+20])