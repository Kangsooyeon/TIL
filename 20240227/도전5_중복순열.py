# path = []
#
# def func(x):
#     if x==3:
#         print(path)
#         return
#
#     for i in range(1,7):
#         path.append(i)
#         func(x+1)
#         path.pop()
#
# func(0)

path = []

def func(x):
    if x==5:
        print(path)
        return

    for i in range(1,5):
        path.append(i)
        func(x+1)
        path.pop()

func(0)