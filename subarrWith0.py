class Solution:
    def maxLen(self, n, arr):
        hm = {}
        s =0 
        ans = 0 
        l = []
        for j in range(n) :
            s+=arr[j]
            if s==0 :
                ans = max(ans,j+1)
            if s in hm :
                ans = max(ans,(j-hm[s]) )
                l.append(arr[hm[s]+1:j+1])
                
            if s not in hm : hm[s] = j
        
        return ans 
                
                
            
a = Solution()
a.maxLen(8,[ 15,-2,2,-8,1,7,10,23]) 
a.maxLen(2,[2,-2])