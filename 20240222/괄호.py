li = list(map(str, input().split("-")))
result = 0

for i in li[0].split("+"):
    result += int(i)

for i in li[1:]:
    for j in i.split("+"):
        result -= int(j)

print(result)