

def func(n,mid,m):
        
        ans = 1
        for i in range(n):
            ans *= mid  
            if ans > m :
                 return 2 
        if ans == m :
            return 0 
        return 1 
def nThroot(n,m):
    

    
    
    l = 0 
    h = m 
     
    while l <= h :
        mid = (l+h)//2
        k = func(n,mid,m)
        if k == 0 :
            return mid 
        if k == 2 :
            h = mid-1
        if k == 1 :
            l= mid+1
            
    return -1 

k = 64**(1/4)
print(k)

n = 3
m = 3**3

print(nThroot(n,m))





    
    
            
            
        
    