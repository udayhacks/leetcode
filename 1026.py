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



import sys
class Solution:
    def __init__(self):
        self.diff = 0

    def maxAncestorDiff(self, root) -> int:
        def dfs(root):
            if not root:
                return [sys.maxsize, -sys.maxsize]

            if root.left == None and root.right == None:
                return [root.val, root.val]
            
            aa = root.val
            left = dfs(root.left)
            right = dfs(root.right)

            minVal = min(left[0], right[0])
            maxVal = max(left[1], right[1])
                
            self.diff = max(self.diff, max(abs(minVal - root.val), abs(maxVal - root.val)))

            minVal = min(minVal, root.val)
            maxVal = max(maxVal, root.val)

            return [minVal, maxVal]
        
        dfs(root)

        return self.diff 
        
        
        
a = Solution()
a.maxAncestorDiff(root)