S = input()
N = len(S)

for i in range(1,N+1):
    if N%i==0:
        if i>N//i:
            break
        R = i
        C = N//i

for i in range(R):
    for j in range(0,N,R):
        print(S[i+j], end='')