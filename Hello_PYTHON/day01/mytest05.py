a = input("출력할 구구단을 입력하시오 : ")
aa = int(a)

multiple = 0
print("<",aa,"단>" )
for i in range(1,9+1):
    multiple = aa * i
    print(f"{a} * {i} = {multiple}")