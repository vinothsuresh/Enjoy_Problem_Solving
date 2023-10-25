arr = [1,2,3]

def prefix_sum(arr):
    n = len(arr)
    prefix_sum = [0] * n
    for i in range(n):
        if i == 0:
            prefix_sum[i] = arr[i]
        else:
            prefix_sum[i] = prefix_sum[i-1] + arr[i]

    total_sum = prefix_sum[n-1]
    for i in range(n):
        if i:
            left_sum = prefix_sum[i-1]
        else:
            left_sum = 0
        right_sum = total_sum - prefix_sum[i]
        if left_sum == right_sum:
            return i
    return -1

print(prefix_sum(arr))