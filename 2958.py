class Solution:
    def maxSubarrayLength(self, nums, k: int) -> int:
        
        i , j = 0, 0

        maxx = 1
        mapp = {}

        while i < len(nums) and j < len(nums):
            
            mapp[nums[j]] = mapp.get(nums[j], 0) + 1

            if mapp[nums[j]] > k:
                maxx = max(j-i, maxx)
                while mapp[nums[j]]>k:
                    mapp[nums[i]] -= 1
                    i = i+1
            
            j += 1 

        return max(maxx, j-i)           


a = Solution()
a.maxSubarrayLength([2,1,3,1,2,3,1,2],2)


