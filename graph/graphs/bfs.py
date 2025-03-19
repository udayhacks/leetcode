#User function Template for python3

from typing import List
from queue import Queue
class Solution:
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V ,E, adj) :
        que = Queue()
        vs= [0]*(V+1)
        ans = []
        que.put(0)
        vs[0] =1
        
        
        while que :
            k = que.get()
            ans.append(k)
            
            
            
            for i in adj[k]:
                if vs[i] == 0 :
                    que.put(i)
                    vs[i] =1
                    
                    
        return ans 
                
            
            
            
a = Solution()

V = 5
E = 4
adj = [[1,2,3],[],[4],[],[]]
k = a.bfsOfGraph(V,E,adj)
print(k)    
        
        