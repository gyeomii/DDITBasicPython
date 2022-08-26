a = input("첫 수를 입력하시오 : ")
b = input("끝 수를 입력하시오 : ")

aa = int(a)
bb = int(b)
#num = range(int(a),int(b)+1)
num = range(aa,bb+1)
print(list(num))
sum = 0
for i in num :
    sum += i
print(a + " ~ " + b + "의 합 :",sum)