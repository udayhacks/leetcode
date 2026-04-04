# Last updated: 04/04/2026, 13:11:56
class Solution:
    def removeStars(self, s: str) -> str:
        stack  = []
        for i in s :
            if stack and i == "*" :
                stack.pop()
                continue 
            stack.append(i)

        return ''.join(stack) 