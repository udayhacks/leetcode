class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0 :
            return 0 
        if n < 0 :
            n= -n 
            x = 1/x 
        result = 1 
        while n > 0 :
            if n %2 == 1 :
                result*= x 

            x *=x
            n //=2 
        return result 
     
     
a = Solution ()
a.myPow(2,-10)
z = pow(2,-10)