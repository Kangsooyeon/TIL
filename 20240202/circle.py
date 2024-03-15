T = int(input())
for tc in range(T):
    N = int(input())

    cnt =0
    for i in range(N+1):
        for j in range(N+1):
            if (i**2 + j**2) <= (N**2) :
                cnt +=1

    result = cnt*4 - 4*N -3
    print(f'#{tc+1} {result}')
