N=3

path = []

def func(lev,start):
    if lev==3:
        print(*path)
        return

    for i in range(start,7):
        path.append(i)
        func(lev+1, i)
        path.pop()

func(0,1)