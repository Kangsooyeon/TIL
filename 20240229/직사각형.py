for _ in range(4):
    x1,y1,x2,y2,x3,y3,x4,y4 = map(int, input().split())

    if x2<=x4:
        length_x = x2-x3
    else:
        length_x= x4-x1

    if y2<=y4:
        length_y = y2-y3
    else:
        length_y= y4-y1

    if length_x<0 or length_y<0:
        print('d')

    elif length_x==0 or length_y==0:
        if length_x==0 and length_y==0:
            print('c')
        else:
            print('b')
    else:
        print('a')