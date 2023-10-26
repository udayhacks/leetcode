class Solution:
    def findMissing(self,arr, size): 
        ans = 0 
        
        for i in range(1,max(arr)) :
            if i not in arr :
                return i 
            
        return size+1
    
    
a = Solution()
a.findMissing([1,2,3,7],4)
        
        
    # your code goes here
