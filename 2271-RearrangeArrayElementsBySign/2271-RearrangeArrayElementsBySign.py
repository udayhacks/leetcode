# Last updated: 04/04/2026, 13:12:07
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos= []
        neg = []
        for i in nums :
            if i>0 :
                pos.append(i)
            else:
                neg.append(i)

        ans = []
        for i in range(len(pos)) :
            ans.append(pos[i])
            ans.append(neg[i])
        return ans        