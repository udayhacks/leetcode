def alphaTriangle(n: int):
    start = 65
    for i in range(1,n+1):
        start= (start+(n-1))
        for j in range(i) :
            print(chr(start),end= "")
            start-=1 
        start = 65
        print() 
        
        
        
alphaTriangle(9)