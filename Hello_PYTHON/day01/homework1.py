from random import randint, random


me = input("홀/짝을 입력하시오 : ")
rnd = randint(0,1)
print(rnd)
com = ""
if rnd == 0:
    com ="홀"
elif rnd == 1:
    com = "짝"
else :
    print("홀/짝을 정확히 입력하세요")

print("user : " + me)
print("com : " + com)
print("<<결과>>")
if me == com : 
    print("User 승리")
else : 
    print("Computer 승리")