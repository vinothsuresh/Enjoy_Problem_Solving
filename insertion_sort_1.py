l = [8,2,5,1,3,7]
n = len(l)
for i in range(1,n):
    ele = l[i]
    j = i-1
    while j>=0 and l[j]>ele:
        l[j+1] = l[j]
        j -=1
    l[j+1] = ele



print(l)