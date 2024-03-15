# 아래 함수를 수정하시오.
def find_min_max(li):
    min_value = li[0]
    max_value = li[0]

    for num in li[1:]:

        if num > max_value:
            max_value=num
        
        if num < min_value:
            min_value=num

    return min_value, max_value



result = find_min_max([3, 1, 7, 2, 5])
print(result)  # (1, 7)