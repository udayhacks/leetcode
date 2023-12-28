
l = [60,20,19,10,40,30,9]




def previousGreater(l):
    stack = []
    print(-1)
    stack.append(l[0])
    
    for i in range(1, len(l)) :
        while len(stack) != 0 and stack[-1]< l[i] :
            stack.pop()   
        print(stack[-1])
        stack.append(l[i])  
        
        
previousGreater(l)   
    