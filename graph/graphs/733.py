class Solution:
    def floodFill(self, image, sr, sc, color) :
        
        from collections import deque 
        from collections  import deque
        m = len(image)
        n = len(image[0])
        rot= [[0 for i in range(n)] for j in range(m)]
        q = deque()
        
        k = image[sr][sc]
        rot[sr][sc] = color
        q.append([sr,sc])
        
        
        while q :
            
            j = q.popleft()                 
            r = j[0]
            c = j[1]
         
            
            dr = [0,-1,0,1]
            dc = [-1,0,1,0]
            
            for i in range(4):
                ar = r+dr[i]
                ac = c+dc[i]
                if (ar >= 0 and ar < m) and (ac >= 0 and ac < n) and  image[ar][ac] == k  and rot[ar][ac]!=color: 
                    
                    rot[ar][ac] =color
                    q.append([ar,ac])
                    
                    
                    
        for i in range(m):
                for j in range(n):
                    if rot[i][j] != color :
                        rot[i][j] =image[i][j]
                        
                        
                        
        return rot
                     
                    
                   
        
        
        
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
color = 2

a= Solution()
if [[2,2,2],[2,2,0],[2,0,1]] == a.floodFill(image, sr, sc, color):
    print(True)
    
else:
    print(False)
        
        
        
        
        
        
        
        
        
        
        
        
        
        