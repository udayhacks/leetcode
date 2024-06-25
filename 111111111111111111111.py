class Solution:
    def minimumArea(self, grid) -> int:
        
        row = len(grid[0])
        col = len(grid)
        l = 0 
        b = 0 
        for i in range(col):
            s =e = 0
            for j in range(row) :
                
                if grid[i][j] == 1 :
                    
                    if s ==- 0 and j ==0 :
                        s = j 
                        b+=1
                    elif s != -1:
                        e = j 
            
                
            l = max(l,(e-s)+1)
            
        return l*b
                  
                  
a= Solution()
a.minimumArea([[1]])