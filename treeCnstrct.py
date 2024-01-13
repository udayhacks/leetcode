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

from inorder import inorder 
#from preOrder import preOrder


def preOrder(root,l=[]):
    if root != None :
        l.append(root.data)
        preOrder(root.left)
        preOrder(root.right)
        return l
        















prl = preOrder(root)
inL = inorder(root)

prL = prl



prL = [1, 2, 4, 7, 8, 5, 9, 3, 6, 7]
inL = [7, 4, 8, 2, 9, 5, 1, 6, 3, 7]

prl_indix = 0 
ios = 0 
ioe = len(inL)-1





def cnstrct ( prL, inL ,ios,ioe):
    if ios > ioe :
        return None
    
    global prl_indix 
    root = node(prL[prl_indix])
    prl_indix+=1
    if ios == ioe :
        return root 
    
    for i in range(ios,ioe+1):
        if inL[i] == root.data :
            break
        
    root.left = cnstrct(prL,inL,ios,i-1)
    root.right = cnstrct(prL,inL,i+1,ioe)
    
    return root

jj = cnstrct(prL, inL ,ios,ioe)


print(inorder(jj))
            



