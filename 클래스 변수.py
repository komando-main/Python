# class Family:
#     lastname = '고'
#     lastname1 = '박'
    
# a=Family()

# # a.lastname='김'

# print(a.lastname)
# print(a.lastname1)

# a.lastname = '김'# a 객체에 lastname 이라는 객채가 새롭게 생성된다

# print(a.lastname)
# print(a.lastname1)


class Human:
        name = 0
        age = 0
        phone = 0
#Human    
class Add(Human):
    def __init__(self, name, age, phone):
        self.name = name
        self.age = age
        self.phone = phone
        
    def name1(self):#변수명과 함수명이 겹치면 안된다 ex)def name() 에러남
        return f"{self.name}"
    
    def age1(self):
        return f"{self.age}"
    
    def phone1(self):
        return f"{self.phone}"
    
    def all(self):
        return [self.name, self.age, self.phone]
    

    
class Add1(Add):
    def name1(self): #함수 재정의
        return f"내 이름은 {self.name} 입니다"
    
    def age1(self):
        return f"나이는 {self.age} 입니다"
    
    def phone1(self):
        return f"휴대폰 번호는 {self.phone} 입니다"

a=Add1('min', 39, '123456789')

print(a.name1())
print(a.all())