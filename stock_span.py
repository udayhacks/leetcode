l = [60,20,19,10,40,30,9]
ans =[1,1,1,1,1,4,1,1]  





def stockSpan(l):
    stack = []
    ans = [1]
    stack.append(0)
    for i in range(1,len(l)):
        while len(stack) != 0 and l[stack[-1]] < l[i] :
            stack.pop()
        k = 1 if len(stack) == 0 else i-(stack[-1])
        ans.append(k)
        stack.append(i)
        
    return ans 

stockSpan(l)
    