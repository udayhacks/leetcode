








# it used to spreading related prblm and bfs using matrix and  modify as per your need uday ...........

def bfs (self,vs,r,c,board) :
        
        from collections import deque
        
        q = deque()
        q.append([r,c])
        row = len(board)
        col = len(board[0])
        
        vs[r][c] = 1 
        dr = [0,-1,0,1]
        dc = [-1,0,1,0]  
       
            
        while q :
            k = q.popleft()
            rr = k[0]
            cc = k [1]
          
            
            for i in range(4):
                ar = rr+dr[i]
                ac = cc+dc[i]
                if (ar >= 0 and ar < row) and (ac >= 0 and ac < col) and vs[ar][ac] ==0 and board[ar][ac] == "O":
                    q.append([ar,ac])
                    vs[ar][ac] = 1
                    
                    
                    
                
                    
                    