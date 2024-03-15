class Dog():
    sound = '멍멍'


class Cat():
    sound = '야옹'


#Dog Class를 우선 상속하였을 경우
class Pet(Dog, Cat):

    def __str__(self) -> str:
        return f'애완동물은 {super().sound} 소리를 냅니다.'
    
pet1 = Pet()
print(pet1)


#Cat Class를 우선 상속하였을 경우
class Pet(Cat, Dog):

    def __str__(self) -> str:
        return f'애완동물은 {super().sound} 소리를 냅니다.'
    
pet2 = Pet()
print(pet2)