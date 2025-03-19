#File create

class Solution:
    def bfsOfGraph(self, adj):
        
        from collections import deque 
        ans = []
        que = deque()
        n = len(adj)
        vst = [0]*n
        
        que.append(0)
        vst[0]= 1
        
        while que :
            front = que.popleft()
            ans.append(front)
            for i in adj[front]:
                if vst[i]== 0 :
                    vst[i]  = 1
                    que.append(i)
        
                
        return ans 
        
        
        
a = Solution()

adj = [[2,3,1], [0], [0,4], [0], [2]]
a.bfsOfGraph(a.bfsOfGraph(adj))