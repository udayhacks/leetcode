def Diameter(root ) :
    if root is None :
        return 0 
    l = Diameter(root.left)
    r = Diameter(root.right)
    m = ((l+r)+1)
    global res
    res = max(res,m)
    return 1+max(l,r)
    
    
    
    
    
    
res = 0
    

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



print(Diameter(root))