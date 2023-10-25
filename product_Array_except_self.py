def productExceptSelf(nums):
        n = len(nums)
        product = [0] * n
        left_product = [0] * n
        right_product = [0] * n
        for i in range(n):
            if i:
                temp = nums[i-1] * left_product[i-1]
                left_product[i] = temp
            else:
                left_product[i] = 1

        right_product[n-1] = 1 
        for j in range(n-2,-1,-1):
            temp = nums[j+1] * right_product[j+1]
            right_product[j] = temp

        for i in range(n):
            product[i] = left_product[i] * right_product[i]
        return product

print(productExceptSelf([2,1,3,4]))