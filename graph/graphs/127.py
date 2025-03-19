class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        from collections import deque 


        q = deque()
        hs = {}
        
        for i in  wordList:
            hs[list(i)] = 0 
            
        q.append([beginWord,1]) 
        
        while q :
            k = q.popleft()
            l = k[0]
            
            if l == endWord :
                return k[1]
            
            l = list(l)
            
            for i in range(len(l)) :
                for j in range(26) :
                    w
                
             
        
         
        
        
        