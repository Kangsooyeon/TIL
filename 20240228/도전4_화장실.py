li = [15, 30, 50, 10]
li.sort()

result = 0
while li:
    result += li[0]*len(li[1:])
    li.pop(0)
print(result)

# person = [15, 30, 50, 10]
# n = len(person)
# person.sort()
# sum=0
# left_person=n-1     #화장실 이용 아직 못한 대기자의 수
#
# for turn in range(n):
#     time = person[turn]
#     sum+=left_person*time
#     left_person-=1
# print(sum)