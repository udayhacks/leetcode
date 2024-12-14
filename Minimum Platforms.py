#User function Template for python3

class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n,arr,dep):
        
        arr.sort()
        dep.sort()
        
        i = 0 
        j = 0 
        ans = cnt = 1
        
        while i < len(arr) and j < len(dep):
            if arr[i] <= dep[j]:
                cnt+=1
                i+=1
            else:
                cnt-=1
                j+=1
                
            ans = max(ans,cnt)
            
        return ans 
            


arr = [900, 945, 955, 1100, 1500, 1800]
dep = [920, 1200, 1130, 1150, 1900, 2000]


a = Solution()
a.minimumPlatform(len(arr),arr,dep)