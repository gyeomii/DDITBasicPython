class Xi:
    def __init__(self):
        self.money = 1000
    def steal(self, smoney):
        self.money += smoney

class Putin:
    def __init__(self):
        self.nuclear = 5000
    def alzheimer(self):
        self.nuclear -= 1

class JungEun:
    def __init__(self):
        self.missile = 10000
    def ssorau(self):
        self.missile -= 100

class Child(Xi, Putin, JungEun):
    def __init__(self):
        Xi.__init__(self)
        Putin.__init__(self)
        JungEun.__init__(self)
        
    def steal(self, smoney):
        super().steal(smoney)
        
    def alzheimer(self):
        super().alzheimer()
        
    def ssorau(self):
        super().ssorau()
        
ch = Child()

print(f"money : {ch.money}, nuclear : {ch.nuclear}, missile : {ch.missile}")
ch.steal(100)
ch.alzheimer()
ch.ssorau()
print(f"money : {ch.money}, nuclear : {ch.nuclear}, missile : {ch.missile}")
