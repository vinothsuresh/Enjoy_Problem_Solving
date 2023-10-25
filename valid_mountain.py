class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        n = len(arr)
        print(n)
        i=0
        if n < 3:
            return False
        while i < n-1:
            if arr[i] < arr[i+1]:
                i=i+1
            else:
                break
        if i == n-1:
            return False
        j = n-1
        while j>=0:
            if arr[j-1] < arr[j]:
                j = j-1
            else:
                break
        if j ==0:
            return False
        if i == j:
            return True
        else:
            return False


obj = Solution()
print(obj.validMountainArray([9,8,7,6,5,4,3,2,1,0]))