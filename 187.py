from collections import defaultdict
class Solution:
    def findRepeatedDnaSequences(self, s):
        n = len(s)
        hast = defaultdict(int)
        res = []
        l = 0
        for r in range(n) :
            if r - l + 1 <10 :
                continue 
            else:
                if r - l + 1 == 10 :
                    hast[s[l:r+1]] +=1
                    l += 1
                   
        
        for key in hast:
            if hast[key] > 1:
                res.append(key)
        return res
    
solution  = Solution()
s2 = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
s1 = "AAAAAAAAAAAAA"
print(solution.findRepeatedDnaSequences(s1))
print(solution.findRepeatedDnaSequences(s2))