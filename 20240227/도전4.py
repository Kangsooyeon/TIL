#branch=2, level=3

def func(x):
    if x==3:
        return
    for _ in range(2):
        func(x+1)

    print(x, end =' ')

func(0)
