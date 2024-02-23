def func(arr):
    temp =  arr.copy()
    for i in range(1,len(arr)):
        for j in range(i):
            if a[i] > a[j] :
                temp[i] = max(a[j],a[i]+a[j]) 
    return max(temp)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
a = [3,4,2,8,10]  