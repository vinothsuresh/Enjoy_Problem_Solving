arr = [1,5,6,3,4,2]
max_area = -1
n = len(arr)
for i in range(n):
    for j in range(i+1, n):
        temp = (j-i) * min(arr[j],arr[i])
        max_area = max(temp,max_area)

print(max_area)