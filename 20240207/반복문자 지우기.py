T = int(input())

for tc in range(1, T+1):
    s = input()
    stack =[]

    for i in range(len(s)):
        stack.append(s[i])
        if len(stack)>1 and stack[-1]==stack[-2]:
            stack.pop()
            stack.pop()
    print(f'#{tc} {len(stack)}')