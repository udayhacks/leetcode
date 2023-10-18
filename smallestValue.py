<<<<<<< HEAD
class Solution:
       def hIndex(self, citations) -> int:
        for i, j in enumerate(sorted(citations, reverse=True)):
            if i >= j:
                return i
        return i + 1
                 
                 

                 
 
a = Solution()
a.hIndex( [1,3,1]) 
a.hIndex( [3,0,6,1,5]) 
=======
class Solution:
       def hIndex(self, citations) -> int:
        for i, j in enumerate(sorted(citations, reverse=True)):
            if i >= j:
                return i
        return i + 1
                 
                 

                 
 
a = Solution()
a.hIndex( [1,3,1]) 
a.hIndex( [3,0,6,1,5]) 
>>>>>>> 86d1479054b46193473a840b95d6acc626908e7b
a.hIndex( [3]) 