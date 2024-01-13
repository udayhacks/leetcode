# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class node:
    def __init__(self ,data):
        self.left = None 
        self.val = data 
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




def pr(root,l =[]):
    if root :
        l.append(root.val)
        pr(root.left,l)
        pr(root.right,l)
        return l
        



l = []
def sq(root):
    if root is None :
        return root 
        
    if root.left == None and root.right == None :
        
        return root
    k = root.val*root.val
    root.val = k
    sq(root.left)
    sq(root.right)
    
    return root


sq(root)


print()       

print(pr(sq(root)))

    