N =int(input())
i=1
start = '666'
while i<N:
    for plus in range(1,N):
        if str(plus)[-1]=='6':
            tmp = str(plus) + ans[-3:-1]

            for num in range(10):
                ans = tmp+ str(num)
                i+=1
        else:
            ans = str(plus) + start
            i += 1
            continue
print(ans)

