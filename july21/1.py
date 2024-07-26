
class Solution:
    def removeOrder(self, n, arr, str) :
        arr.sort()
        ans = []
        
        for i in range(n):
            if str[i] == "0" :
                ans.append(arr[i])
            else:
                ans.append(arr[-i])
                
        return ans
                
                
a = Solution()

n = 4
ar= [7 ,5 ,11 ,3]
s = "0110"
a.removeOrder(n,ar,s)
