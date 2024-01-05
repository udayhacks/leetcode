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



def isBalancedMain(root) :
    if isBalanced(root)  == -1 :
        return False
    return True 

def isBalanced(root) :
    if root is None :
        return 0 
    l = isBalanced(root.left)
    if l == -1 :
        return -1 
    r = isBalanced(root.right)
    if r == -1 :
        return -1 
    if abs(l-r) >1 :
        return -1 
    return max(l,r)+1


a = isBalancedMain(root)
print(a)

