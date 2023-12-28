class node:
    def __init__(self,data = 0, next = None)  :
        
        
        
        self.data = data 
        self.next  = next
        
        
        
    
    
    
a = node(1)
b = node(2,a)
c = node(3,b)
d = node(4,c)



p = d 
k = c 
for i in range(1):
    p = p.next
    k = k.next 
    
print(p.next.next.data,k.data)