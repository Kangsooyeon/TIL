T = int(input())
for tc in range(T):
    li = list(map(str, input()))
    stack = []
    for i in range(len(li)):
        if stack and stack[-1]=='(' and li[i]==')':
            stack.pop()
        else:
            stack.append(li[i])
    if stack:
        print('NO')
    else:
        print('YES')