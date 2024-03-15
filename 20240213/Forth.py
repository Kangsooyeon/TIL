T = int(input())
for tc in range(1, T+1):
    li = list(map(str, input().split()))
    stack = []

    try:
        for i in li:
            if i.isdigit():
                stack.append(i)
            elif i in '+-*/':
                b= int(stack.pop())
                a= int(stack.pop())
                if i=='+':
                    stack.append(a+b)
                elif i=='-':
                    stack.append(a-b)
                elif i=='*':
                    stack.append(a*b)
                elif i=='/':
                    stack.append(a//b)
            else:
                break

        if len(stack) == 1:
            print(f'#{tc} {int(stack.pop())}')
        else:
            print(f'#{tc} error')

    except:
        print(f'#{tc} error')