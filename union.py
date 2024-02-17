def sortedArray(a, b) :

    union_arr = []
    i = j = 0 
    while i <len(a) and j <len(b) :
        aa = a[i]
        bb = b[j]
        if aa <= bb :
        
            if aa not in union_arr :
                union_arr.append(aa)
            i+=1
        
        else:
            if bb not in union_arr:
                union_arr.append(bb)
            j+=1


    while i <len(a):
        if a[i] not in union_arr:
            union_arr.append(a[i])
        i+=1

    while j <len(b):
        if b[j] not in union_arr:
            union_arr.append(b[j])
        j+=1

    return union_arr


    
sortedArray([1,2,3,4,6],[2,3,5])