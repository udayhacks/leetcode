def inorder(root,l = []) :
    if root != None :
        inorder(root.left)
        l.append((root.data))
        inorder(root.right)
        return l 
        
        
        
        
        
class node:
    def __init__(self,data) :
        self.left = None 
        self.data = data 
        self.right = None 
        
        
        




a = node(10)
b = node(20)
c = node(40)
d=node(50)
e = node(60)
f = node(70)
g = node(30 )
h = node(32) 
i = node(21)




a.left = b
a.right = g
b.left = c
b.right = d

d.left = e
d.right = f

g.left = h
g.right = i




