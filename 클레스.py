# class FourCal:
#     pass

# a=FourCal()
# print(type(a))

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
    

a=FourCal(4,5)
# a.setdate(4,5)
print(f"first:{a.first}, second:{a.second}")
print(f"first + second = {a.add()}")
print(f"first * second = {a.mul()}")
print(f"first - second = {a.sub()}")
print(f"first / second = {a.div()}")