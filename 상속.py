
# class MoreFourCal(FourCal): #상속받을 클래스 위에 정의하면 못 읽는다
#     def pow(self):
#         return self.first ** self.second

class FourCal:
    def __init__(self, first, second):
        self.first=first
        self.second=second

    # def setdate(self, first, second):
    #     self.first = first
    #     self.second = second
    
    def add(self):
        return self.first + self.second
    
    def mul(self):
        return self.first * self.second
    
    def sub(self):
        return self.first - self.second
    
    def div(self):
        return self.first / self.second

class MoreFourCal(FourCal):
    def pow(self):
        return self.first ** self.second
    
    def div(self):
        if self.first == 0 or self.second == 0:
            return 0
        else:
            return self.first / self.second 

a=MoreFourCal(4,5)
# a.setdate(4,5)
print(f"first:{a.first}, second:{a.second}")
print(f"first + second = {a.add()}")
print(f"first * second = {a.mul()}")
print(f"first - second = {a.sub()}")
print(f"first / second = {a.div()}")
print(f"first ** second = {a.pow()}")
