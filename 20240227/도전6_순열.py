path1=[]
path2=[]
used = [0]*7
def type1(x): #중복순열
    if x==N:
        print(path1)
        return

    for i in range(1,7):
        path1.append(i)
        type1(x+1)
        path1.pop()


def type2(x): #순열
    if x == N:
        print(path2)
        return

    for i in range(1, 7):
        if used[i]==1:
            continue
        used[i]=1
        path2.append(i)
        type2(x + 1)
        path2.pop()
        used[i]=0

N, Type = map(int, input().split())
if Type==1:
    type1(0)
elif Type==2:
    type2(0)