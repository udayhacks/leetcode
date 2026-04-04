# Last updated: 04/04/2026, 13:10:38
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