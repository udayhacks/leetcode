
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





def leav (root,res = []) :
    if root :
        k = root.data
        if root.left is None and root.right is None :
            res.append(root.data)
            return res 
        
        leav(root.left ,res)
        leav(root.right,res)
        
        return res
        
        
print(leav(root,[])) 



root1 = a
root.left = b
root.right = c 
b.left = d
b.right= e
c.left = g
c.right= f 
d .left = f 
d.right  = i
e.left = h


print(leav(root1,[])) 
print([1,2]==[2,1])
print(leav(root,[])==leav(root1,[]))