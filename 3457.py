


class Solution:
    from math import ceil
    def maxWeight(self, pizzas) -> int:
        n = len(pizzas)
        days = n//4 
        odd_days = days//2
        if( days%2 !=0 ) :odd_days = 1+days//2
    
        pizzas.sort()
        ans = 0 
        
        for i in range(days):
            if odd_days:
                ans+=pizzas[n-1]
                n = n-1
                odd_days-=1
            else:
                ans+=pizzas[n-2]
                n = n-2

        return ans 
                
                
arr = [5,5,4,4,3,3,3,2,2,2,2,1]
sol = Solution()
sol.maxWeight(arr)
