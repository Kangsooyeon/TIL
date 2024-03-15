#실습 4
number_of_people = 0

def increase_user():
    pass

def create_user(name, age, address):

    user_info={'name':name, 'age':age, 'address':address }
    print(f'{name}님 환영합니다!')

    return user_info

name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조x 선', '나주', '한성부']

info_zip=list(zip(name, age, address))
print(info_zip)
print(list(map(lambda x : create_user(*x), info_zip)))