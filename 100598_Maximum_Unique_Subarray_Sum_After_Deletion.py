#File create
class Solution:
    def maxSum(self, nums):

    
        ans = float('-inf')
        for i in range(len(nums)):
            map = {}
            sum = 0 
            for j in range(i,len(nums)):
                if nums[j] not in map :
                    sum+=nums[j]
                    map[nums[j]] = 0 
                ans = max(ans,sum)
        return ans
    
a = Solution()
print(a.maxSum( [1,2,-1,-2,1,0,-1]))
print(a.maxSum( [-1000]))
                
            
        