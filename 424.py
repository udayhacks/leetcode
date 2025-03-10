""" from collections import Counter ,deque
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        maxVal = 0 
        maxfreq = 0 
        for i in s :
            if i in freq :
                freq[i] +=1 
                if maxfreq <freq[i]:
                    maxfreq = freq[i]
                    maxVal = i
            else:
                freq[i]=1
                 
                 
        n = len(s)
        Val = 0
        
        i = 0 
        l = 0 
        f = False
        for j in range(n) :
            mj= s[j]
            if mj!= maxVal and  l<=k :
                l+=1
            
            while mj != maxVal and l>k and s[i]== maxVal:
                i+=1
                f = True
            if f :
                i+=1
                f = False
            
            Val = max(Val,j-i+1)
            
        return Val 
        
        
        
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        maxVal = 0 
        maxfreq = 0 
        for i in s :
            if i in freq :
                freq[i] +=1 
                if maxfreq <freq[i]:
                    maxfreq = freq[i]
                    maxVal = i
            else:
                freq[i]=1
                 
                 
        n = len(s)
        Val = 0
        
        if maxfreq == 0:
            return k+1
        
      
        
        l = 0 
        h= 0 

        for r in range(n):
            if s[r] != maxVal and h <=k :
                h+=1
            
            while s[r] != maxVal and h > k :
                if s[l] == maxVal :
                    l+=1
                else:
                    l+=1
                    h-=1

            if h <=k :
                Val = max(Val,r-l+1)

        return Val

            
 """ 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqs = defaultdict(int)
        res = 0
        i = 0

        for j in range(len(s)):
            freqs[s[j]] += 1
            maxFreq = max(freqs.values())
            curLen = j - i + 1
            if curLen - maxFreq > k:
                freqs[s[i]] -= 1
                i += 1
            res = max(res, j - i + 1)
        
        return res            
a = Solution()
#print(a.characterReplacement("ABAB",2))
print(a.characterReplacement("ABCDE",1))