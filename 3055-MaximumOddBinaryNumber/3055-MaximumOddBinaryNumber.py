# Last updated: 04/04/2026, 13:11:20
class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        s = list(s)
        j = s.count("1")
        a= [0]*len(s)
        for i in range(j-1):
            a[i] = 1
        
        a[-1] = 1
        
        anss = ""
        for i in a :
            anss+=str(i)
        
        return anss
        