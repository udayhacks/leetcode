class Solution:
    def maxScore(self, cardPoints,k):
        total = sum(cardPoints)
        ans = 0 
        l = 0 
        res =0
        n = len(cardPoints)
        for i in range(n):
            ans +=cardPoints[i]
            if i-l+1 == n-k :
                res= max(res,total-ans)
                ans-=cardPoints[l]
                l+=1
        return res

a = Solution()
print(a.maxScore([2,2,2],2))