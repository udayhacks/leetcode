def rainWaterTrapingInContinueBar(l):
    res= 0 
    n = len(l)
    lmax= [0]*n
    rmax = [0]*n
    lmax[0] = l[0]
    
    
    for i in range(1,n):
        lmax[i] = max(l[i],lmax[i-1])
    
    rmax[n-1] = l[-1] 
    for i in range(n-2 ,-1,-1) :
        rmax[i]= max(l[i],rmax[i+1])

    
    for i in range(1,n-1):
        res += min(lmax[i],rmax[i]) -l[i]
        
    return res
        
        
rainWaterTrapingInContinueBar([5,0,6,2,3])
        
        
        