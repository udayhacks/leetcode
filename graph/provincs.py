#User function Template for python3
from collections import deque
class Solution:
    
    
    def path_check(self,ans,i,vst):
        que = deque()
        que.append(i)
        vst[i] = True
        
        while que :
            front = que.popleft()
            for  j in ans[front]:
                if vst[j]  == False :
                    vst[j] = True
                    que.append(j)
                    
        
        
    
    
    def numProvinces(self, adj, V):
        
        n = len(adj)
        ans = [[] for i in range(n)]
        
        for  i in range(n):
            for j in range(n):
                if adj[i][j] == 1 and i ==j  :
                    ans[i].append(j)
                    ans[j].append(i)
                elif adj[i][j]  ==1 :
                     ans[i].append(j)
                    
        vst = [False]*(n)
        
        province = 0 
        for i in range(n):
            if vst[i]==False :
                province+=1
                self.path_check(ans,i,vst)
        
        return province
                    
        
        
        
a = Solution()
Input=[
    

[1, 0],
[0 ,1]
]

a.numProvinces(Input,2)