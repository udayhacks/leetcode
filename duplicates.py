def original(s):
    #finding original values 
    
    res = 0
    for i in range(1, len(s)) :
        if s[res] != s[i]:
            res+=1
    return res+1
    
    
    
    
k = original([1,2,2,2,2,5]) 