from collections import deque
class Solution:
    
    #Function to return list containing vertices in Topological order.
    
    
    
    
    def dfs(self,i,vs,adj,que):
        
        vs[i] = 1
        for j in adj[i] :
            if vs[j] == -1:
                self.dfs(j,vs,adj,que)
                
        que.append(i)
            
            
            
        
        
        
    
    
    
    def topoSort(self, V, adj):
        
        vs=[-1]*V
        ans = []
        que = deque()
        
        for i in range(V) :
           if vs[i] == -1 :
               self.dfs(i,vs,adj,que)
               
               
        while que :
             ans.append(que.pop())
             
             
             
        return ans
            
        
        