from random import randint


def getOddEven():
    res = ""
    rnd = randint(0,1)
    if rnd == 0:
        res = "홀"
    else:
        res = "짝"
    return res

me = input("홀/짝 중 선택 : ")
com = getOddEven()
print(f"com : {com}") 
if me == com:
    print("USER 승리")
else:
    print("COM 승리")