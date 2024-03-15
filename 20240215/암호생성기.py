for tc in range(1, 11):
    N = int(input())
    li = list(map(int, input().split()))

    i=1
    while True:
        if i>5:
            i=1
        else:
            front=li.pop(0)
            rear = front-i
            if rear<0:
                rear=0
            li.append(rear)
            i+=1

        if rear<=0:
            break
    print(f'#{tc}', *li)