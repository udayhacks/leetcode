# Last updated: 04/04/2026, 13:11:06
class Solution:
    def divideArray(self, nums,k) :
        nums.sort()
        n = len(nums)
        res = []
        
        i =j= 0 
        while i <n :
            kk = max((nums[i+2]-nums[i+1]),(nums[i+2]-nums[i]))
            if kk > k :
                return []
            res.append([nums[i],nums[i+1],nums[i+2]])
            i+=3
            
            
        return res
                
            
                
        