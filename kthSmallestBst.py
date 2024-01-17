





from ast import Nonlocal


class bst :
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None 
        
    
 


    
    
    
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
        
        
        

root  = bst(5)
for i in [5,3,6,2,4,1] :
    Insert(root,i)
    
    
printT(root)







# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

        
        
        
 
        


class Solution:
    def smallerNumbersThanCurren(self, root, k: int) -> int:
        self.counter = 1
        self.ans = None
        
        def small(root):
            
            if root is None  or self.ans :
                return 
            aa= root.val
            small(root.left)
            if self.counter == k :
                self.ans = root.val 
                return 
            small(root.right)
            
        small(root)
        return self.ans
                
                 
        


        
    
    
a= Solution()
 

k = a.kthSmallest(root,3)

print(k)

