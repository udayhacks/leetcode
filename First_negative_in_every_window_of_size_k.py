#User function Template for python3

class Solution:
    def FirstNegativeInteger(self, arr, k):
        neg = []
        ans =[]
        n = len(arr)
        i =0 
        j = 0 
        p = 0 
        while j <n :
            if arr[j] <0 :
                neg.append(arr[j])
            if j-i+1 < k :
                j+=1
                
            else:
                if p <len(neg):
                    ans.append(neg[p])
                else:
                    ans.append(0)
                if p <len(neg) and neg[p] == arr[i]:
                    p+=1
                i+=1
                j+=1
                
        return ans 
                    
                
a = Solution()
print(a.FirstNegativeInteger([12, -1, -7, 8, -15, 30, 16, 28],3))