l = [12,34,45,15]
#l = [1,2,3,4,5,6]



def second(ls):
    
    ll = None 
    l = ls[0]
    i = 1
    j = len(ls) -1
    
    while i <=j :
        k = max(ls[i],ls[j])
        if l < k :
            ll = l
            l = k 
        elif l > k  :
            if ll == None or ll< k :
                ll = k 
                
        i+=1
        j-=1 
        
    return (l , ll)


second(l)