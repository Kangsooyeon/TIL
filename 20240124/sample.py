class Circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14*self.r*self.r
    
    def __str__(self):
        print(f'[원] radius: {self.r}')
    

c1 = Circle(10)
c2 = Circle(1)

print(c1)
print(c1.area())