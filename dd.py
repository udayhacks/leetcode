class Solution:
    def sumIndicesWithKSetBits(self, nums, k) -> int:
        s= 0 
        for i in range(len(nums)):
            j = bin(i)
            h = j[:].count("1")
            if h == k :
                s+=nums[i]
        return s
                
        
a = Solution()
a.sumIndicesWithKSetBits([5,10,1,5,2], 1)