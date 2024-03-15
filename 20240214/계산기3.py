for tc in range(10):
    N = int(input())
    infix = input()
    op = {'+': 1, '-': 1, '*': 2, '/': 2}

    postfix = []
    stack = []
    result = []

    for s in infix:
        if s.isdigit():
            postfix.append(s)
        elif s == '(':
            stack.append(s)
        elif s == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()  # pop '('
        else:
            while stack and op.get(stack[-1], 0) >= op.get(s, 0):
                postfix.append(stack.pop())
            stack.append(s)
    while stack:
        postfix.append(stack.pop())

    for p in postfix:
        if p.isdigit():
            result.append(p)
        else:
            b = int(result.pop())
            a = int(result.pop())
            if p =='+':
                result.append(a + b)
            elif p =='*':
                result.append(a * b)
    print(f'#{tc+1} {result[0]}')