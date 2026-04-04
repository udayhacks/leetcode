# Last updated: 04/04/2026, 13:11:24
class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        c = 0 
        for i in range(len(nums)) :
            for j in range(i+1,len(nums)) :
                if nums[i]+nums[j] < target :
                    c +=1
        return c
        
        
        