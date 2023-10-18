<<<<<<< HEAD
def original(s):
    #finding original values 
    
    res = 0
    for i in range(1, len(s)) :
        if s[res] != s[i]:
            res+=1
    return res+1
    
    
    
    
=======
def original(s):
    #finding original values 
    
    res = 0
    for i in range(1, len(s)) :
        if s[res] != s[i]:
            res+=1
    return res+1
    
    
    
    
>>>>>>> 86d1479054b46193473a840b95d6acc626908e7b
k = original([1,2,2,2,2,5]) 