N = 5
li = [[0]*7 for _ in range(2)]

for i in range(4):
    li[0][i] = N+i
    li[1][6-i] = N-i
print(li)