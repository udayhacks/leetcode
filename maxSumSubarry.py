<<<<<<< HEAD







def maxSubarr(l):
    res = -10**5
    n  = len(l)
    s =l[0]
    res= s
    
    
    for i in range(1, n ):
        s = max(s+l[i],l[i])
        res = max(s,res)
        
        
    return res


l = [-3,8,-2,4,-5,6]



def maxSumAtIndex(l ,k):

    res = -10**5
    n  = len(l)
    s =[0]*n 
    s[0] = l[0]
    
    for i in range(1, n):
        
        s[i] = max(s[i-1]+l[i],l[i])
        
    return max(s[:k])
        
        
    
        
l = [-3,8,-2,4,-5,6] 
k = 5 

      
maxSumAtIndex(l ,5)  
        
        

        
l = [-3,8,-2,4,-5]   
        
        
        
        
maxSubarr(l)
=======







def maxSubarr(l):
    res = -10**5
    n  = len(l)
    s =l[0]
    res= s
    
    
    for i in range(1, n ):
        s = max(s+l[i],l[i])
        res = max(s,res)
        
        
    return res


l = [-3,8,-2,4,-5,6]



def maxSumAtIndex(l ,k):

    res = -10**5
    n  = len(l)
    s =[0]*n 
    s[0] = l[0]
    
    for i in range(1, n):
        
        s[i] = max(s[i-1]+l[i],l[i])
        
    return max(s[:k])
        
        
    
        
l = [-3,8,-2,4,-5,6] 
k = 5 

      
maxSumAtIndex(l ,5)  
        
        

        
l = [-3,8,-2,4,-5]   
        
        
        
        
maxSubarr(l)
>>>>>>> 86d1479054b46193473a840b95d6acc626908e7b
        