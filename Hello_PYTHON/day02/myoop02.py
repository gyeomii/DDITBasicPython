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

class SungWoo(Xi, Putin, JungEun):
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
        
sw = SungWoo()

print(f"money : {sw.money}, nuclear : {sw.nuclear}, missile : {sw.missile}")
sw.steal(100)
sw.alzheimer()
sw.ssorau()
print(f"money : {sw.money}, nuclear : {sw.nuclear}, missile : {sw.missile}")
