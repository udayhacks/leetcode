l = [60,20,50,40,10,50,60]

# navie approch
def largestHistogram(l) :
    res = 0 
    for i in range(len(l)) :
        curr = l[i]
        
        for j in range(i-1,-1,-1):
             if l[i] <= l[j]:
                curr +=l[i]
             else:
                break 
            
            
            
        for j in range(i+1,len(l)):
            if l[i] <= l[j]:
                curr +=l[i]
            else:
                break
            
            
        res = max(res, curr)
    
    return res 
                            







largestHistogram(l)




















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