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
                
            
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
a= Solution()
a.divideArray( [1,3,4,8,7,9,3,5,1],2)
a.divideArray([1,3,3,2,7,3],3)
        