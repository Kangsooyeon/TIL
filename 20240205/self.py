generate_li =[]
num_li = list(range(1, 10000))

for i in range(1,10000):
    str_i =list(map(int, str(i)))
    generate_li.append(i+sum(str_i))

result = list(set(num_li) - set(generate_li))
result.sort()
print(*result, sep='\n')
