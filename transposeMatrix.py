a = [ 
     
    [1,2,3] ,
    [4,5,6] ,
    [7,8,9]
    
]



"""a = [
    
    [1,2],
    [1,2]
    
]"""

def transpose(a):
    for i in range(len(a)):
        for j in range(len(a)) :
            print(a[j][i] , " ", end = "")
        print() 
        
        
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
           
        for i in range(c-1,-1) :
            print(a[c-1][i],end= "")
        
        for i in range(c-2,0):
            print(a[0][i],end = "")


        
boundaries(a)   
        
    