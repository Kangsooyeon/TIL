# 아래 함수를 수정하시오.
def even_elements(li):
    result =[]
    for i in li:
        print(i)
        if i % 2==0:
            temp=li.pop(li.index(i))
            result.extend([temp])

    return result
    


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)