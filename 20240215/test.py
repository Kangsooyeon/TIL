li1=[]
li2=[]
with open("output.txt", "r") as f:
    for line in f:
        li1.append(line)

with open("output (10).txt", "r") as f:
    for line in f:
        li2.append(line)

print(list(set(li2).difference(li1)))