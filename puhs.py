class Solution:
    def buttonWithLongestTime(self, events)  :
        ans = events[0][0]
        check= events[0][1]
        n = len(events)
        for i in range(1,n):
            j,k = events[i]
            p = events[i-1][1]
            
            if check < (k-p) :
                ans = j 
                check = (k-p)
            elif check == (k-p):
                ans = min(ans,j) 
            
        return ans 
    
a = Solution()
a.buttonWithLongestTime([[12,2],[8,3],[18,5],[4,6],[3,7],[1,9],[2,17],[18,20]])    
   
        