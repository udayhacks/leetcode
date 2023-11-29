class Solution:
    def longestConsecutive(self, nums):
        nums.sort()
        j = 0
        ans = 0
        if len(nums) == 0 :
            return 0
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] == 1 :
                j +=1 
                ans = max(ans , j )
            elif nums[i+1] == nums[i] :
                continue
            else :
                j = 0 

        return ans+1 









class Solution:
    def longestConsecutive(self, nums):
        f = set(nums)
        ans= 0 
        
        for i in nums :
            if i-1 not in f :
                l = 0 
                while (i+l)in f :
                    l+=1 
                l = max (l,ans)


        return ans 
                
        
                  
        
        
a = Solution()
k = [1,2,0,1] 
a.longestConsecutive(k)
