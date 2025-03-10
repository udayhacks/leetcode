


class solution ():
    def ans(self,A):
        stack = []
        res = []
        for i in A:
            while stack and stack[-1] >= i:
                stack.pop()
            if stack:
                res.append(stack[-1])
            else:
                res.append(-1)
            stack.append(i)
        return res
    
    
    
    
a = solution()
a.ans([34,35,27,42,5,28,39,20,28])      
   