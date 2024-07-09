class Solution:

    def func(self,mid,arr):
        import math
        ans = 0 
        for i in arr :
            ans+=math.ceil(i/mid)
        return ans 


    def minEatingSpeed(self, piles, h: int) -> int:
        small = large =  piles[0]
        for i in piles :
            small = min(small ,i)
            large = max(i , large)

        while small <= large :
            mid = (small+large)//2
            k = self.func(mid,piles)
            if k <= h :
                large= mid-1
            else:
                small = mid+1

        return small
            

a = Solution()
piles = [312884470]
h = 312884480
print(a.minEatingSpeed(piles,h))