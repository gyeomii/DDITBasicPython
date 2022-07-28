arr=[1,2,3]

#shallow copy - 어설픈 copy
brr = arr
#copy() - deep copy
crr = arr.copy()

arr[0] = 0

print("arr", arr)
print("brr", brr)
print("crr", crr)