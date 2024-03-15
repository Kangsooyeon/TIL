# arr=['A','B','C','D','E']
#
# for a in range(5):
#     start1 = a+1
#     for b in range(start1, 5):
#         start2 = b+1
#         for c in range(start2, 5):
#             print(arr[a], arr[b], arr[c])

arr=['A','B','C','D','E']
path = []

n=3
def run(lev, start):
    if lev==n:
        print(*path)
        return

    for i in range(start, 5):
        path.append(arr[i])
        run(lev+1, i+1)
        path.pop()

run(0,0)