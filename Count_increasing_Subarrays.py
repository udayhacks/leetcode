class Solution:
    def countIncreasing(self, arr):
        
        ans = 0 
        start =0 
        end = 1 
        n = len(arr)
        while end <n :
            if arr[end-1] <arr [end]:
                ans +=(end-start)
            if arr[end-1]>= arr[end]:
                start = end 
                
            end+=1
            
        return ans 
            
            
            
a = Solution()
arr = [1, 3, 3, 2, 3, 5]
print(a.countIncreasing(arr))
            