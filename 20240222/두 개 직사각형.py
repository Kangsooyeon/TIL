T = int(input())
for tc in range(1,T+1):
    rec_1=list(map(int, input().split()))
    rec_2=list(map(int, input().split()))

    if rec_1[2]>rec_2[0] and rec_1[3]>rec_2[1]:
        result =1
    elif (rec_1[2]==rec_2[0] and rec_1[3]>rec_2[1]) or (rec_1[3]==rec_2[1] and rec_1[2]>rec_2[0]):
        result =2
    elif rec_1[2]==rec_2[0] and rec_1[3]==rec_2[1]:
        result =3
    else:
        result =4
    print(rec_1)
    print(rec_2)
    print(f'#{tc} {result}')
