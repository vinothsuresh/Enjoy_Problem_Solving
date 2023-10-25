arr = [20,10,8,6,4,2]
n = len(arr)
for i in range(0,n,2):
    if i > 0 and arr[i] < arr[i-1]:
        arr[i],arr[i-1] = arr[i-1], arr[i]
    if i < n-1 and arr[i] < arr[i+1]:
        arr[i],arr[i+1] = arr[i+1],arr[i]


print(arr)

        
