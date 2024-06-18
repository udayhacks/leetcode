class Solution:
    def checkSubarraySum(self, nums, k: int) -> bool:

        n = len(nums) 
        if n <= 1:
            return False
        if n ==2 :
            return sum(nums)%k ==0 

        ans =nums[0]+nums[1]
        h = {}
        h[0] = nums[0]
              
        for i in range(1,n):
            ans+=nums[i]
            if ans%k == 0 :
                return True 
            if i-2 >=0 and (ans-h[i-2]) %k == 0 :
                return True 
        
            h[i] = ans  

        return False




a= Solution()
aa= [0,0]
k = 6
a.checkSubarraySum(aa,k)