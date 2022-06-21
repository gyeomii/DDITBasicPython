class Animal:
    def __init__(self, age):
        self.age = age
    
    def HappyBirth(self):
        self.age += 1
        return self.age

class Human(Animal):
    def __init__(self, age, money):
        self.age = age
        self.money = money
        
    def Albamon(self):
        self.money += 1
        return self.money