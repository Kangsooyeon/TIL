di=[0,1,0,-1] #우하좌상 result%4
dj=[1,0,-1,0]

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    li = [list(map(int, input().split())) for _ in range(N)]
    result = 0

    #찾아야 할 번호 리스트 생성 및 정렬
    num = []
    for i in range(N):
        for j in range(N):
            if li[i][j]:
                num.append(li[i][j])
    num.sort()

    #해당 번호를 찾으면 pop(0)
    i=0
    j=0

    while num:
        l=1
        k=result%4
        L = len(num)

        #우회전 1번 했을 때 있을 경우
        c1=1
        while 0 <= i + di[k] * c1 < N and 0 <= j + dj[k] * c1 < N:
            ni = i + di[k] * c1
            nj = j + dj[k] * c1

            c2=1
            while 0 <= ni + di[(k+1)%4] * c2 < N and 0 <= nj + dj[(k+1)%4] * c2 < N:
                ti = ni + di[(k+1)%4] * c2
                tj = nj + dj[(k+1)%4] * c2
                if li[ti][tj] ==num[0]:
                    i = ti
                    j = tj
                    num.pop(0)
                    result +=1
                    break
                else:
                    c2+=1
            if L==len(num):
                c1+=1
            else:
                break
        #그래도 없다? 직진해서 부딪히면 우회전
        if L==len(num):
            l=1
            while 0 <= i + di[k] * l < N and 0 <= j + dj[k] * l < N:
                ni = i + di[k] * l
                nj = j + dj[k] * l
                l += 1
            i=ni
            j=nj
            result +=1

    print(f'#{tc} {result}')