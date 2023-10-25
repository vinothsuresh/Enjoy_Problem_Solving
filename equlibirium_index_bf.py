class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        prefix_sum = [0] * n
        for i in range(n):
            if i == 0:
                prefix_sum[i] = nums[i]
            else:
                prefix_sum[i] = prefix_sum[i-1] + nums[i]

        total_sum = prefix_sum[n-1]
        for i in range(n):
            if i:
                left_sum = prefix_sum[i-1]
            else:
                left_sum = 0
            right_sum = total_sum - prefix_sum[i]
            if left_sum == right_sum:
                return i
        return i

        

obj = Solution()
print(obj.pivotIndex([-7,1,5,2,-4,3,0]))