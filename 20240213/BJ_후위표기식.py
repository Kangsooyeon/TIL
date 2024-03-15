infix = input()
op = {'+': 1, '-': 1, '*': 2, '/': 2}

result = []
stack = []

for s in infix:
    if s.isalpha():
        result.append(s)
    elif s == '(':
        stack.append(s)
    elif s == ')':
        while stack and stack[-1] != '(':
            result.append(stack.pop())
        stack.pop()  # pop '('
    else:
        while stack and op.get(stack[-1], 0) >= op.get(s, 0):
            result.append(stack.pop())
        stack.append(s)

while stack:
    result.append(stack.pop())

print(''.join(result))