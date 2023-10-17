class Solution:
       def hIndex(self, citations) -> int:
        for i, j in enumerate(sorted(citations, reverse=True)):
            if i >= j:
                return i
        return i + 1
                 
                 

                 
 
a = Solution()
a.hIndex( [1,3,1]) 
a.hIndex( [3,0,6,1,5]) 
a.hIndex( [3]) 