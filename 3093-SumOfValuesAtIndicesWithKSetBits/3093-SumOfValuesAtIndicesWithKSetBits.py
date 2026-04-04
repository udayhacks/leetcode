# Last updated: 04/04/2026, 13:11:19
class Solution:
    def sumIndicesWithKSetBits(self, nums, k) -> int:
        s= 0 
        for i in range(len(nums)):
            j = bin(i)
            h = j[:].count("1")
            if h == k :
                s+=nums[i]
        return s