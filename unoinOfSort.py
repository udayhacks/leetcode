def union_sort(a,b):
    i =j= 0
    l = []
    
    
    while i < len(a) and j <len(b):
        
        
        if  a[i] == a[i+1] :
            i +=1
        if b[j] == b[j+1] :
            j +=1
        if a[i] <= b[j] :
            if a[i] == b[j]:
                l.append(a[i])
                i+=1
                j+=1
            else:
                l.append(a[i])
                i+=1
        else :
            l.append(b[j])
            j+=1
            
            
    while i <len(a) :
         if l[-1] != a[j]:
            l.append(a[i])
         i+=1
    while j < len(b):
        if l[-1] != b[j]:
            l.append(b[j]) 
        j+=1
        
            
    return l 




a = [1,3,6,7,7]
b = [3,5,6,9,10,10]


union_sort(a,b)

             

    
    