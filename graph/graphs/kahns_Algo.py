
    
from collections import deque 

class Solution:
    
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        
        
        que = deque()
        incom = [0]*V
        ans = []
        
        for i in range(V):
            for j in adj[i]:
                incom[j] +=1
                
                
                
        for i in range(V) :
            if incom[i] == 0 :
                que.append(i)
                
                
        while que :
            k = que.popleft()
            ans.append(k)
            for i in adj[k]:
                incom[i]-=1
                if incom[i] == 0 :
                    que.append(i)
                        
        return ans 
            
        
        
        
       