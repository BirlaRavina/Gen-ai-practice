def merge_sort(lst):
    if len(lst) > 1:
        
        mid = len(lst)//2
        leftlst = lst[:mid]
        rightlst = lst[mid:]

        merge_sort(leftlst)
        merge_sort(rightlst)
        i = j = k = 0
        while i<len(leftlst) and j<len(rightlst):
            if leftlst[i]<rightlst[j]:
                lst[k] = leftlst[i]
                i+=1
            else:
                lst[k] = rightlst[j]
                j+=1
            k+=1
        while i<len(leftlst):
            lst[k] = leftlst[i]
            i+=1
            k+=1
        while j<len(rightlst):
            lst[k] = rightlst[j]
            j+=1
            k+=1
    return lst
lst = [22,3,44,22,1,45,6,7,77,75,4]
print(merge_sort(lst))