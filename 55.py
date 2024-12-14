class Solution:
    def jump(self, nums):
        
        
        
        k = []

        k.append(nums[0])
        for i in range(1, len(nums)):
            k.append(max(k[i-1],nums[i]))
            
            
            
            
        c = 0    
        i = 0
        while i <len(nums):
            c+=1
            i = i+k[i]
            
        return c
            
            
            
            
            
            
            
            
            



a = Solution()
l = [a.jump([2,3,1,1,4]),a.jump([3,2,1,0,4]),a.jump([1,3,2])]



for i in l:
    print(i)