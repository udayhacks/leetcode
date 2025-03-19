def dfsOfGraph(self, adj):
        
         
        ans = []
        que = []
        n = len(adj)
        vst = [0]*n
        
        que.append(0)
        vst[0]= 1
        
        while que :
            front = que.pop()
            ans.append(front)
            for i in adj[front]:
                if vst[i]== 0 :
                    vst[i]  = 1
                    que.append(i)
        
                
        return ans 