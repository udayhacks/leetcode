class Solution:
    def countNegatives(self, grid):
        c = 0
        for i in range(len(grid)):
            l= 0 
            h = len(grid[i])-1

            while l < h:
                m = (l+h)//2 

                if grid[i][m] >= 0 :
                    l = m+1 
                
                elif grid[i][m] < 0 :
                    
                    if grid[i][m-1] > 0 :
                        break
                    else:
                        h = m-1 
    
                
            c +=(len(grid[i])-m+1)                        
            


          

        return c 

grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
#grid = [[3,2],[1,0]]





a = Solution()
a.countNegatives(grid)