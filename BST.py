


class bst :
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None 
        
    
l = [4,2,5]

root = bst(l[0])
    
    
    
def search(root,k):
    if root is None :
        return False
    
    aa = root.val
    if root.val == k :
        return True 
    elif k < root.val :
        return (root.left,k )
    else :
        return search(root.right, k)
        
        
        
        
def Insert(root,k):
    if root is None:
        return bst(k)
    if k < root.val :
        root.left =Insert(root.left ,k)
    elif k > root.val :
        root.right = Insert(root.right, k )
    return root 
        

def printT(root):
    if root :
        printT(root.left)
        print(root.val,end = "")
        printT(root.right)

Insert(root,2)
printT(root)



l = [3,5,4,9,7]


for i in range(len(l)):
    Insert(root,l[i])
    
    
printT(root)
import bstDelete

bstDelete.delete(root,4)
print()
printT(root)
print()

import floorBSt
r = floorBSt.floorBst(root,8)
print(r)
