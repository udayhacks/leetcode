def Solution(N,P):
    sum =0 
    P = list(P)
    count = 0
    n = len(P)
    for i in range(n-1,-1,-1):
        if P[i] == 'W':
            sum +=1
            
            
    for i in range(n):
        if sum == 0 :
            return count 
        if P[i] == 'S':
            if n == sum :
                return 1 
            
            count +=1
        else:
            sum -=1
            
        
            
        
    return count 
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
N= 10
P = 'SSWWSWWSWW'
print(Solution(N,P))