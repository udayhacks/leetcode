def solve(A, B):
        
        b = B-1
        new = 0 
        
        d = []
        for i in range(len(A)):
            if A[i] == 1 :
                k = i-b
                j = i+b
                d.append([k,j])
                
        k = 1
        if  d[0][0] != 0 :
            return -1
        j = 0
        for i in range(1,len(d)):
            
            if d[0][1] +1 == d[i][0]:
                k+=1
                d[0][1] = d[i][1]
                
        if d[0][1] >= len(A)-1:
            return k 
        return -1
                
                
            
            
            
            
            
                
print(solve( [ 0, 0, 0, 1, 0],3))
        