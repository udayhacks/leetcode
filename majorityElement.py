def majorityElement(arr) : 
    
    #major element of arr 
    maj = None 
    count = 0 
    for i in arr :
        if count == 0  :
            maj = i 
        if i == maj :
            count +=1 
        else :
            count -=1 
        
    count  =  0 
    #major element of arr majority greater than n//2 
    for i in arr :
        if i == maj :
            count +=1 
    if count  > len(arr)//2 :
        return maj 
    return -1  




majorityElement([1,2,2,2,4])