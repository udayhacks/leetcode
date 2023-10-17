class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0 or n ==1 :
            return 0 
        value = [True] *n
        value[0] = value[1] = False
        c = 0 
        for i in range(2, n):
            if value[i] :
                c+=1
                for j in range(2*i, n , i):
                    value[j] = False

        return c 
     


a = Solution()
a.countPrimes(10)