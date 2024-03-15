for tc in range(10):
    N = int(input())
    S = input()

    stack = []
    result = []
    postfix = ''

    for s in S:
        if s.isdigit():
            postfix +=s
            if stack:
                postfix+=stack.pop()
        else:
            stack.append(s)

    for p in postfix:
        if p.isdigit():
            result.append(p)
        else:
            b=int(result.pop())
            a=int(result.pop())
            result.append(a+b)

    print(f'#{tc+1} {result[0]}')