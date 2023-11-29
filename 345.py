class Solution:
    def reverseVowels(self, s: str) -> str: 
        s = list(s)
        v = ['a','e','i','o','u','A','E','I','O','U']
        k = []
        for i in s :
            if i in v :
                k.append(i)
                
                
        k.reverse()
        h = len(k)
        j = 0 
        for i in range(len(s)):
            if s[i] in v  and j < h:
                s[i] = k [j]
                j+=1 
                
        return s
            
            
           
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
s = "aA"
e ="holle"
        
        
        
a = Solution()
a.reverseVowels(s)