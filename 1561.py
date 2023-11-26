class Solution:
    def maxCoins(self, piles) -> int:
        sorted_piles = sorted(piles)
        j = len(piles)//3
        big_piles = sorted_piles[j:]
        b = big_piles[::3]
        maxxed = sum(b)
        return maxxed 
    
    
    



a= Solution()
a.maxCoins([2,4,1,2,7,8])  
k = [2,4,1,2,7,8,0]
m = k[::3]
