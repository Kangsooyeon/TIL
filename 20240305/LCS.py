s1 = input()
s2 = input()
L1 = len(s1)
L2 = len(s2)

j=0
cnt = 0
result = []

for i in range(L1):
    while j<L2:
        j_save=0
        if s1[i]==s2[j]:
            j+=1
            j_save=j
            cnt +=1
            print(i,j,s1[i])
            break
        else:
            j+=1
    if j==L2:
        if j_save==L2:
            j=0
            print(cnt)
            result.append(cnt)
            cnt = 0

        else:
            j=j_save
result.append(cnt)
print(result)