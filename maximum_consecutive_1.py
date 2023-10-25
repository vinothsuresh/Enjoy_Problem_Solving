def findMaxConsecutiveOnes(nums):
        count = 0
        max_count = 0
        for i in range(len(nums)):
            if nums[i]:
                count +=1
            else:
                max_count = max(max_count,count)
                count = 0
        return max(max_count,count)
        

print(findMaxConsecutiveOnes([1,1,0,1,1,1,0,0,1]))