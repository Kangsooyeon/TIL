for tc in range(1, 11):
    N, s = map(str, input().split())
    stack = []

    for i in range(len(s)):
        stack.append(s[i])
        if len(stack) > 1 and stack[-1] == stack[-2]:
            stack.pop(-1)
            stack.pop(-1)
    stack = ''.join(stack)
    print(f'#{tc} {stack}')