# Last updated: 04/04/2026, 13:10:34
class Solution:
    def maximumPossibleSize(self, nums: List[int]) -> int:
        stack = []
        c= 0 
        for i in nums:
            if (len(stack) == 0 ) or (stack[-1]<= i) :
                stack.append(i)
                c+=1
                

        return c
            