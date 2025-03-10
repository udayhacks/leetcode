import heapq
class Solution:

    def kthSmallest(self, arr,k):
        heapq.heapify(arr)
    
        return arr
        
        
        
a = Solution()
p = a.kthSmallest([7, 10, 4, 3, 20, 15],3)
print(p)