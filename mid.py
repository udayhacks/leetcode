#User function Template for python3

class Solution:
    #Complete this function
    def power(self,N,R):
        res=1
        mod=10**9+7
        while R>0:
            if R%2==1:
                res=(res*N)%mod
            N=(N*N)%mod
            R//=2
        return res








a= Solution()
a.power(16,61)


def power(N, P):
 
    
    if P == 0:
        return 1
 
    
    if P%2 == 0:
        
      result = power(N, P//2)%((10**9)+7)
      return (result * result)%((10**9)+7)
    else :
      result = power(N, (P-1)//2)%((10**9)+7)
      return ((N%((10**9)+7) ) * (result * result )) %((10**9)+7)
  
  
  
  
  
power(16,61)
 
























