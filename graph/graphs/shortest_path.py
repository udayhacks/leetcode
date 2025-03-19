#User function Template for python3




from collections import deque
from sys import maxsize
class Solution:
    
    def shortestPath(self, edges, n, m, src):
        adj = []
        
        for i in range(n):
            adj.append([])
        for i in range(len(edges)) :
            k,j = edges[i]
            adj[k].append(j)
            adj[j].append(k)
            
            
                
    
        from collections import deque 
        from sys import maxsize
        ds=[maxsize]*n
        que = deque()
        que.append(src) 
        ds[src] = 0 
        vs=[-1]*n
        
        
        while que :
            p = que.popleft()
        

            
            for i in adj[p] :
                if ds[p]+1 < ds[i] :
                    ds[i] = ds[p]+1
                    que.append(i)
                
                    
        
                
                
        for i in ds:
            if i == maxsize :
                i = -1
                
        return ds
                
                
                
                
n = 9
m = 10
edges=[[0,1],[0,3],[3,4],[4,5],[5,6],[1,2],[2,6],[6,7],[7,8],[6,8]] 


a= Solution()
a.shortestPath(edges,n,m,0)