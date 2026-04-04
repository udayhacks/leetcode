# Last updated: 04/04/2026, 13:10:28
class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        n = n *n 
        cap = n*w
        if cap <maxWeight:
            return n
        else:
            return maxWeight//w
        
        