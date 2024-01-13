#         self.right = r
# 
# 
# 
# 
# ight




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
a = node(10)
b = node(2)
c = node(13)
d = node(20)
e = node(15)
g = node(6)
f = node(78)
h = node(80)
i = node(9)

root = c
root.left = b
root.right = a
b.left = d
b.right= e
a.left = g
a.right= f 
d .left = f 
d.right  = h
e.left = i







class Solution:

    def getMinimumDifference(self, root) -> int: 

        ans = 10**5
        def r(root,ans):
            if root:
                aa = root.val
                
                if root.left and root.right :
                    ans =min(ans,abs(root.val-root.right.val),abs(root.val-root.left.val))
                elif root.left:
                    ans =  min(ans,abs(root.val-root.left.val))
                elif root.right:
                    min(ans,abs(root.val-root.right.val))    
                r(root.left,ans)
                r(root.right,ans)
                return ans    


            
        
        
        return r(root,ans)
    
    
a= Solution()
l = a.getMinimumDifference(root)
        
print(l)
        
        
        