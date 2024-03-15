def f(i,k):
    if i==k:
        return
    else:
        print(li[i])
        f(i+1, k)

li = [10, 20, 30]
N =len(li)
f(0, N)