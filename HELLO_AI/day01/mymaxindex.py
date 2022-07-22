arr = [0, 1, 3, 1, 1,  1, 2, 2, 2, 2]

max_idx = -1
max = -1

for idx, num in enumerate(arr):
    if(num > max):
        max = num
        max_idx = idx

print("max_idx", max_idx)
