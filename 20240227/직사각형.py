T = int(input())

for tc in range(1,T+1):
    x1, y1, x2, y2 = map(int, input().split())
    x3, y3, x4, y4 = map(int, input().split())

    if x2<=x4:
        length_x = x2-x3
    else:
        length_x= x4-x1

    if y2<=y4:
        length_y = y2-y3
    else:
        length_y= y4-y1

    if length_x>0 and length_y>0:
        result =1
    elif length_x==0 and length_y==0:
        result = 3
    elif length_x==0 or length_y==0:
        result=2
    else:
        result =4

    print(f'#{tc} {result}')
