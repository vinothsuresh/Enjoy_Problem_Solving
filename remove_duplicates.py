arr = [2,2,2,2,2,3,3,3]

def remove_sorted(arr):
    j = 1
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            arr[j] = arr[i]
            j +=1

    return j


print(remove_sorted(arr))