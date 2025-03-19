from typing import List

from collections import deque
class Solution:
    
    
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
            
            q = deque()
            vs = [0]*(V+1)
            q.append([0,-1])
            vs[0]=1
            
            while q :
                k = q.popleft()
                l = k[0]
                m = k[1]
                for i in adj[l]:
                    if vs[i] == 0 :
                        q.append([i,l])
                    
                    
                
                    elif 
                       
                        
            return False
            
	    
     
a = Solution()
adj = [[1], [0, 2, 4], [1, 3], [2, 4], [1, 3]]
a.isCycle(len(adj),adj)
	    