class node:
    def __init__(self ,data):
        self.left = None 
        self.data = data 
        self.right = None 
        
        
k = [1,2,3,4,5,6,7,8,9]
a = node(1)
b = node(2)
c = node(3)
d = node(4)
e = node(5)
g = node(6)
f = node(7)
h = node(8)
i = node(9)


root = a
root.left = b
root.right = c 
b.left = d
b.right= e
c.left = g
c.right= f 
d .left = f 
d.right  = h
e.left = i






def width(root) :
    if root is None :
        return 
    
    
    a = []
    
    a.append(root) 
    res = 0 
    while a :
        count = len(a)
        for i in range(count):
            curr = a.pop(0)
            if curr.right :
                a.append(curr.right)
            if curr.left :
                a.append(curr.left)
                
        res = max(res, count)
    return res 




width(root)