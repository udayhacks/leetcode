<<<<<<< HEAD

class Solution:
    def minSubArrayLen(self, target: int, nums):
        i = 0 
        j= 0 
        s = 0 
        ans = 10**6
        for j in range(len(nums)):
            if s < target :
                s+=nums[j]
            if s >= target :
                while s>= target :
                    ans = min(ans ,j-i)
                    s-=nums[i]
                    i +=1
        if ans==10**6:
            return 0
        return ans+1
            
            
        
        
        
        
target = 11
nums = [2,3,1,2,4,3]
nums = [2,3,1,2,4,3]
nums = [1,1,1,1,1,1,1,1]


target = 4
nums = [1,4,4]

a = Solution()
=======

class Solution:
    def minSubArrayLen(self, target: int, nums):
        i = 0 
        j= 0 
        s = 0 
        ans = 10**6
        for j in range(len(nums)):
            if s < target :
                s+=nums[j]
            if s >= target :
                while s>= target :
                    ans = min(ans ,j-i)
                    s-=nums[i]
                    i +=1
        if ans==10**6:
            return 0
        return ans+1
            
            
        
        
        
        
target = 11
nums = [2,3,1,2,4,3]
nums = [2,3,1,2,4,3]
nums = [1,1,1,1,1,1,1,1]


target = 4
nums = [1,4,4]

a = Solution()
>>>>>>> 86d1479054b46193473a840b95d6acc626908e7b
a.minSubArrayLen(target,nums)