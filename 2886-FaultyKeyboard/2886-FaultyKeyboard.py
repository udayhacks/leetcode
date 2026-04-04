# Last updated: 04/04/2026, 13:11:26
class Solution:
    def finalString(self, s: str) -> str:
        l = []
        for i in s :
            if i == "i":
                l= l[::-1]
            else:
                l.append(i)
                
        return "".join(l)

        