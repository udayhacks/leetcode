class Solution:
    def updateMatrix(self, mat):
        from collections import deque
        
        row = len(mat)
        col = len(mat[0])
        
        q = deque()
        dr = [0,-1,0,1]
        dc = [-1,0,1,0]     
        vs = [[0 for i in range(col)] for j in range(row)]
        ans =[[0 for i in range(col)] for j in range(row)]
        
        for i in range(row) :
            for j in range(col) :
                if mat[i][j] == 0 :
                    vs[i][j] =1
                    ans[i][j] = 0
                    q.append([i,j,0])
                    
                    
        
        while q :
            k = q.popleft()
            r = k[0]
            c = k [1]
            t = k[2]
            ans[r][c] = t 
            
            for i in range(4):
                ar = r+dr[i]
                ac = c+dc[i]
                if (ar >= 0 and ar < row) and (ac >= 0 and ac < col) and vs[ar][ac] ==0 :
                    q.append([ar,ac,t+1])
                    vs[ar][ac] = 1
                    
                    
        return ans
                    
                
                
                
                    
                            
        
                
        
        
        
        
        
        
        
        
        
        
a = Solution()
k = a.updateMatrix([[0,0,0],[0,1,0],[0,0,0]]) 
k = a.updateMatrix([[0,0,0],[0,1,0],[1,1,1]])
k= a.updateMatrix([[1,0,1,1,0,0,1,0,0,1],[0,1,1,0,1,0,1,0,1,1],[0,0,1,0,1,0,0,1,0,0],[1,0,1,0,1,1,1,1,1,1],[0,1,0,1,1,0,0,0,0,1],[0,0,1,0,1,1,1,0,1,0],[0,1,0,1,0,1,0,0,1,1],[1,0,0,0,1,1,1,1,0,1],[1,1,1,1,1,1,1,0,1,0],[1,1,1,1,0,1,0,0,1,1]])
print(k)