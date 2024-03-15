num_dict = {'0001101':0,'0011001':1,'0010011':2,'0111101':3, '0100011':4,
            '0110001':5, '0101111':6, '0111011':7, '0110111':8, '0001011':9}

T = int(input())
for tc in range(1,T+1):
    N,M = map(int, input().split())
    li = [input() for _ in range(N)]
    ans = []
    result = 0

    for i in range(N):
        if li[i].count('0')==M:
            continue
        else:
            tmp = li[i]
            break

    for j in range(M-1, 0,-1):
        if tmp[j]=='1':
            tmp=tmp[j-55:j+1]
            break

    for j in range(0,55,7):
        if tmp[j:j + 7] in num_dict.keys():
            ans.append(num_dict[tmp[j:j + 7]])

    for k in range(8):
        if (k+1)%2==1:
            result += ans[k]*3
        else:
            result += ans[k]

    if result%10==0:
        print(f'#{tc} {sum(ans)}')
    else:
        print(f'#{tc} 0')
