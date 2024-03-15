def func(x):
    if x==6:
        return
    print(x, end=' ')
    func(x+1)
    print(x, end=' ')

func(0)