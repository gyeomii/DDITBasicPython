import time

class Cat:
    def __init__(self):
        print("constructor")
        
    def crying(self):
        print("crying")    
    
    def __del__(self):
        print("destroyer")
    
    def __str__(self):
        return "mew"

c = Cat()
c.crying()
time.sleep(4)
print(c)