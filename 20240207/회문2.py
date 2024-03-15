for _ in range(1,11):
    tc=int(input())
    li = [list(map(str, input())) for _ in range(100)]

    ans =1

    for i in range(100):
        for j in range(100):
            k=ans
            while j+k<=100:
                tmp =''.join(li[i][j:j + k])
                if tmp==tmp[::-1]:
                    ans=max(ans, len(tmp))
                k+=1

    li2 =[list(x) for x in zip(*li)] #전치
    for x in range(100):
        for y in range(100):
            z=ans
            while y+z<=100:
                tmp2 =''.join(li2[x][y:y + z])
                if tmp2==tmp2[::-1]:
                    ans=max(ans, len(tmp2))
                z+=1

    print(f'#{tc} {ans}')