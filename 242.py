class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        d = {}
        h = {}
        for i in range(len(s)):
            k = s[i]
            if k not in d :
                d[k] =1
            else:
                d[k]+=1 
                
                
        for i in t :
            if i not in h :
                h[i] = 1
            else:
                h[i]+=1
           
      
       
        for i in h :
                if d.get(i,-1)!= d.get(i,0) :
                    return False
        return True 

    
            
a = Solution()
s = "anagram"
t = "nagaram"
a.isAnagram(s,t)