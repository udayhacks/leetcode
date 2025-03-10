
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k == len(num):
            return '0'
        stack = []
        ans = ''
        for i in num:
            while stack and k >0 and int(stack[-1]) > int(i):
                stack.pop()
                k -=1 
            stack.append(i)

        while k >0 :
            stack.pop()
            k-=1
            


        

        ans = ''.join(stack).lstrip('0')
        if len(ans):
            return ans 
        return '0'

a = Solution()
print(a.removeKdigits('1432219',3))
print(a.removeKdigits('10200',1))
print(a.removeKdigits('10',1))
print(a.removeKdigits('112',1))