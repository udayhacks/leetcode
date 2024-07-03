def nThroot(n,m):
    
    def func(n,mid,m):
        ans = 1
        for i in range(n):
            ans *= mid
            
            if ans > m :
                 return 2 
             
            if ans == m :
                return 0 
        return 1 
    
    
    l = 0 
    h = m 
    while l< h :
        mid = (l+h)//2
        k = func(n,mid,m)
        if k == 0 :
            return mid 
        if k == 2 :
            l = mid-1
        if k == 1 :
            h= m+1
            
    
    return -1 



n = 4 
m = 64




    
    
            
            
        
    