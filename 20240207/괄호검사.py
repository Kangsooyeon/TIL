start = ["{", "("]
end = ["}",")"]

T = int(input())
for tc in range(1, T+1):
    s = input()
    stack =[]

    for i in s:
        if i in start:
            stack.append(i)

        elif i in end:
            if start[end.index(i)] not in stack:
                result = 0
                break
            elif stack[-1]==start[end.index(i)]:
                stack.pop()
                result = 1

    if stack:
        result =0

    print(f'#{tc} {result}')
