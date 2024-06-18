
class Solution:
    def countSuperPalindrome(self, l : int, r : int) -> int:
        
        
        def palindrome(n):
                    k = str(n)
                    i = 0 
                    l = len(k)-1
                    while i <=l  :
                        if k[i] != k[l-1]: return False
                        i+=1
                        l-=1
                    
            
        ans = 0 
        import math
            
        for i in range(l,r+1):
            k = i**0.5
            if palindrome(i) and k**2 ==i :
                ans+=1
                
        return ans 
    



def palindrome(n):
                    k = str(n)
                    i = 0 
                    l = len(k)-1
                    while i <=l  :
                        if k[i] != k[l]: return False
                        i+=1
                        l-=1
                    return True
                    
                    
palindrome(121)