
def max_container(height):
        max_area = -1
        n = len(height)
        i = 0
        j = n-1
        while i<j:
            curr_area = (j-i)* min(height[i],height[j])
            max_area = max(curr_area, max_area)
            if height[i] > height[j]:
                j-=1
            else:
                i+=1
        return max_area


print(max_container([1,5,6,3,4,2]))