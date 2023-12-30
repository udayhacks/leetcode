l = [60,20,50,40,10,50,60]

# navie approch





























#efficent solution 
def largestHistogram (l):
    
    stack = []
    res = 0 
    
    for i in range(len(l)):
        
        while stack and l[i] <= l[stack[-1]] :
            pop = stack[-1]
            stack.pop()
            curr = (i-stack[-1]-1) if stack else i 
            value = (curr*l[pop])
            res= max(res,value)
        stack.append(i) 
        
        
    while stack :
        pop = stack[-1]
        stack.pop()
        curr = (len(l)-stack[-1]-1) if stack else i 
        value = (curr*l[pop])
        res= max(res,value)
        
    return res

largestHistogram(l)