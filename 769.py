class Solution:
    def maxChunksToSorted(self, arr):
        

        stack = [] 
        j = 0 
        ans = 10**5


        for i in range(len(arr)) :
            
                if  ( not stack  ) or (stack and stack[-1] < arr[i] ) :
                    stack.append(arr[i])
                    ans = min(ans,len(stack))
                    continue

            
                 
                stack = []
                stack.append(arr[i])

        return ans
    
    
    
    
a = Solution()
k = a.maxChunksToSorted([1,5,2,3,4,6,0])
print(k)