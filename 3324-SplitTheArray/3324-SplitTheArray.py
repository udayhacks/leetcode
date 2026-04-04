# Last updated: 04/04/2026, 13:11:03
class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        k = {}
        for i in nums :
            if i in k :
                k[i] +=1
                if k[i]> 2 :
                    return False
                
            else:
                k[i] = 1
                
        return True
        
        