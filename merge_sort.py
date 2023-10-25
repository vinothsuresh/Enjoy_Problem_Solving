def merge_sort(l):
    if len(l) > 1:
        mid = len(l)//2
        larr = l[:mid]
        rarr = l[mid:]
        merge_sort(larr)
        merge_sort(rarr)
        i = 0
        j = 0
        k = 0
        while i < len(larr) and j < len(rarr):
            if larr[i] < rarr[j]:
                l[k] = larr[i]
                i +=1
            else:
                l[k] = rarr[j]
                j +=1
            k+=1

        while i < len(larr):
            l[k] = larr[i]
            i+=1
            k+=1
        
        while j < len(rarr):
            l[k] = rarr[j]
            j+=1
            k+=1
    
l = [7,3,9,5,4,8,0,1]
merge_sort(l)
print(l)