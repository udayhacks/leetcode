from collections import OrderedDict
class Solution:
    def compressedString(self, word: str) -> str:
        

        d = OrderedDict()
        for i in word:
            if i in d :
                d[i]+=1
            else:
                d[i] = 1 
                
        l = []
                
                
        
                
        
            
        for i ,j in d.items():
            if j >9 :
                l.append(str(9))
                l.append(i)
                l.append(str(j-9))
                l.append(i)
                
            else:
                l.append(str(j))
                l.append(i)
                
        return "".join(l)
    
    
a = Solution()
word = "aaaaaaaaaaaaaabb"
a.compressedString(word)