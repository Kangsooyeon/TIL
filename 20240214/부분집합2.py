def f(i,k,s,t):   #k개의 원소를 가진 배열A, 부분집합 합이 t인 경우
    if s==t:    #목표값이면
        for j in range(k):
            if bit[j]:  #A[j]가 포함된 경우
                print(A[j], end= ' ')
        print() #부분집합 출력
    elif i==k: #모든 원소를 고려했으나 s!=t
        return
    elif s>t: #고려한 원소의 합이 t보다 큰 경우
        return
    else:
        for j in range(1, -1, -1):
            bit[i]=j
            f(i+1, k, s+A[i]*j, t)

        # bit[i]=1
        # f(i+1, k, s+A[i], t)
        # bit[i]=0
        # f(i+1, k, s, t)

N = 3
A = [1,2,3,4,5,6,7,8,9,10]
bit = [0]*N     #bit[i]는 A[i]가 부분집합에 포함되는지 표시
f(0,N,0,6)