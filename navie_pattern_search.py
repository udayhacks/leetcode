def navie_Pattern (s, p )  :
    n = len(s)
    m = len(p)
    for i in range(n-m+1) :
        condition = s[i:i+m]
        if condition == p :
            print(f'start from {i}  and ends with {i+m}') 
            
    
    
            
            
            
            
            
            
            
            
            
            
            
            
            
            
s = "abcaasddcaff"
p = "dca" 
navie_Pattern(s,p)