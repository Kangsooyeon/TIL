T = int(input())

for tc in range(1, T+1):
    N = int(input())
    li = input()

    cnt_list=[0]*10

    for i in range(N):
        cnt_list[int(li[i])] +=1

    print(f'#{tc} {9-cnt_list[::-1].index(max(cnt_list))} {max(cnt_list)}')