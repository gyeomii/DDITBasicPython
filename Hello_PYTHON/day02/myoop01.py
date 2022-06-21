class Animal:
    def __init__(self, age):
        self.age = age
    
    def happyBirth(self):
        self.age += 1
        

class Human(Animal):
    def __init__(self, age, money):
        self.age = age
        self.money = money
        
    def albamon(self):
        self.money += 1
        
# Human 객체 생성 (Animal 상속받음)
h = Human(1, 10000)

print(f"나이 : {h.age}")
print(f"자산 : {h.money}")
print("happyBirth, albamon 실행")
h.albamon()
h.happyBirth()

print(f"나이 : {h.age}")
print(f"자산 : {h.money}")