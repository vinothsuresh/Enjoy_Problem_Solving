def count_buildings_facing_sun(arr):
    count = 1
    current_max = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > current_max:
            count +=1
            current_max = arr[i]

    return count


print(count_buildings_facing_sun([7,4,8,2,9]))
print(count_buildings_facing_sun([2,3,4,5]))