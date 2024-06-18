class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        n = len(s) 
        p = [0]*n
        if s[0] == "(":
            p[0] = 1
        
        for i in range(1,n):
            if s[i] == "(":
                p[i] = p[i-1]+1 
                
        ss= [0]*n        
        if s[n-1] ==")":
            ss[n-1] = 1 
            
        for  j in range(n-2, -1,-1):
            if s[j] == ")":
                ss[j] = ss[j+1] +1
                
            
            
                
                
                
a= Solution()
a.minRemoveToMakeValid("a)b(c)d")