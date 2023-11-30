a = [ 
     
    ["a","b","c","d"] ,
    ["e","f","g","h"],
    ["i","j","k","l"] ,
    ["m","n","o","p"]
]



"""a = [
    
    [1,2],
    [1,2]
    
]"""

def transpose(a) :
    pass 
    
        
def boundaries(a) :
    c = len(a[0])
    r = len(a)
    
    if c == 1 :
        for i in range(c):
            print(a[i][0],end = " ")
      
    elif r ==1 : 
          print(*a[0])  
          
    else :
        for i in range(c):
            print(a[0][i],end = '')
        for i in range(1,c-1):
            print(a[i][-1],end = '')
        i = 0   
        for i in range(c-1,-1 ,-1) :
            print(a[r-1][i],end= "")
        
        for i in range(c-2,0,-1):
            print(a[i][0],end = "")   
            
    print()
            
            
            
            
def shapeBoun(a) : 
    c  = len (a[0])
    r = len(a)
    for i in range(r) :
        for  j in range(c) :
            if i== 0 or i== r-1 :
                print(a[i][j],end = '')
            else:
                if j ==0 or j ==c-1:
                    print(a[i][j],end="") 
                else:
                    print("_",end = "")
                
        print()
                    
    

            
        
        
boundaries(a)   
shapeBoun(a)
        
    