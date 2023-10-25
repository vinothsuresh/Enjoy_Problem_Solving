a = [18,110,210,452,546,756,810,500,101,13]
#a = [1,2,3,4,5]
start = 0
end = len(a)-1
while start<=end:
    mid = (start+end)//2
    if a[mid] > a[mid-1] and (mid == end):
         print(a[mid])
         break
    if a[mid] > a[mid+1] and a[mid] > a[mid-1]:
         print(a[mid])
         break
    elif a[mid-1] > a[mid] > a[mid+1]:
         end = mid-1
    else:
         start = mid+1 
     