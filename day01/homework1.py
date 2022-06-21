from random import random


me = input("홀/짝을 입력하시오 : ")
rnd = random()
com = ""
if rnd >= 0.5:
    com ="홀"
elif rnd < 0.5:
    com = "짝"
else :
    print("홀/짝을 정확히 입력하세요")

print("user : " + me)
print("com : " + com)

if me == com : 
    print("User 승리")
else : 
    print("Computer 승리")