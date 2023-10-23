#User function Template for python3

class Solution:
    
    #Function to find maximum number of consecutive steps 
    #to gain an increase in altitude with each step.
    def maxStep(self,A, N):
        
        ans =  0 
        count = 0 
        
        for i in range(N-1) :
            if A[i] < A[i+1] :
                count+=1
                
                
            elif A[i] >= A[i+1] :
                count = 0 
                
            ans = max(count,ans)
                
                
        return ans 
            
            
a = Solution()
a.maxStep(
[9 ,9 ,4 ,3 ,2 ,4 ,5 ,2 ,6],9)