def repeatedNumber(s) :
    # with O(n) and O(n) 
    n = len(s)
    dem = [False] *n 
    
    for i in range(n):
        if dem[s[i]]:
            return s[i] 
        dem[s[i]] = True 
        
        
        








def repeatedNumbers(s) :
    
    #with O(n)  and O(1)
    pass








s = [1,0,2,4,2]

repeatedNumber(s) 