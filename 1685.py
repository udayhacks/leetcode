class Solution:
    def getSumAbsoluteDifferences(self, nums):
        prev = 0
        nex = sum(nums)
        ans = []
        n = len(nums)
        for i in range(len(nums)):
            #since it's sorted we subtract reversely for the elements before the current element
            #i = 0
            #2-2 + 3-2 + 5-2 = 4( 10- 2*(len(nums)))
            #i = 1 2-3 + 3-3 + 5-3 = 1 which is not correct
            # we reverse in prev 3-2+3-3+5-3
            ans.append( nex - (nums[i]*(n-i)) +(i*nums[i])-prev)
            prev += nums[i]
            nex -= nums[i]
        return ans        
       
        

            

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
nums = [2,3,5]
o= [4,3,5] 


a= Solution()
a.getSumAbsoluteDifferences(nums)