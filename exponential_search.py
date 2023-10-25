arr = [21,27,32,41,52,68,71,89,95]


def exponential_search(arr,target):
    n = len(arr)
    if arr[0] == target:
        return 0
    else:
        i = 1
        while i < n:
            if arr[i] < target:
                i = i*2
            elif arr[i] == target:
                return i
            else:
                l = i//2
                r = i
                while l<=r:
                    mid = (l+r)//2
                    if arr[mid] < target:
                        l = mid+1
                    elif arr[mid] > target:
                        r = mid-1
                    else:
                        return mid
                    

target = 41
print(exponential_search(arr,target))

