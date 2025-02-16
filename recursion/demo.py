from collections import deque
def func(items,query):
    d= {}
    n = len(items)
    n = len(items)
    for i in range(len(items)):
        if items[i] in d :
            d[items[i]].append(i)
        else:
            d[items[i]] = deque()
            d[items[i]].append(i)
            
    for i in query:
        if i < 0 :
            i = i*(-1)
            if i in d :
                items[d[i][0]]  = "#"
                d[i].popleft()
            
                
        else:
            items.append(i)
            if i in d :
                d[i].append(n)
                
            else:
                d[i]= deque()
                d[i].append(n)
                
            n= n+1
                
    ans = []
    for i in items :
        if i !="#":
            ans.append(i)
    
    return ans
        
        
              
    
    
    
            
            
i = [1,2,1,2,1]
q = [-1,-1,3,4,-3]
       
k = func(i,q)
print(k)