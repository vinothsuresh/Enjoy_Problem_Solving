arr = [4,8,0,0,2,0,1,0]
zero = 0
for i in range(len(arr)):
    if arr[i] != 0:
        arr[zero], arr[i] = arr[i], arr[zero]
        zero+=1
    

print(arr)