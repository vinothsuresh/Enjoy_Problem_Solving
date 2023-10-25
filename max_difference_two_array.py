arr = [1,4,9,5,3,7]
def maximumDifference(nums):
        min_value = nums[0]
        max_diff = -1
        for i in range(1,len(nums)):
            if (nums[i] - min_value) > max_diff and (nums[i] - min_value) > 0:
                max_diff = nums[i] - min_value
            if nums[i] < min_value:
                min_value = nums[i]

        return max_diff


print(maximumDifference(arr))