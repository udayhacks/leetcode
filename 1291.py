class Solution:
    def sequentialDigits(self, low: int, high: int) -> :
        
        ans = []
        k = len(str(high))
        def helper(ans,val):
            if val > high :
                return 
            if val in range(low,high+1) :
                ans.append(val)
                
            for i in range(1,k)
        