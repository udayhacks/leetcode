class Solution:
    def sortColors(self, nums) :
        
        z = o = t = 0 
        for i in nums :
            if i == 0 :
                z+=1
            if i == 1:
                o +=1
            if i == 2 :
                t +=1
                
        i = 0 
        n = len(nums)
        while i < n  and z > 0 :
            nums[i]= 0 
            z-=1
            i+=1
            
        while i < n  and o> 0 :
            nums[i]= 1
            o-=1
            i+=1
        while i < n  and t > 0 :
            nums[i]= 2
            t-=1
            i+=1
            
        
            


        return nums 
    
    
a= Solution()
a.sortColors([1,2,2,0,0,0])
