class Solution:
    def pseudoPalindromicPaths (self, root) -> int:
        self.count = 0
        self.dp(root, 0)
        return self.count

    def dp(self, node, path):
        aa = node.val
        path = path ^ (1<<node.val)
        if node.left is None and node.right is None:
            if path & (path - 1) == 0:
                self.count += 1
                return
        if node.left is not None:
            self.dp(node.left, path)
        if node.right is not None:
            self.dp(node.right, path)




class node :
    def __init__(self,data):
        self.left = None 
        self.right = None 
        self.val = data 
        
        
        


k = []

for i in [2,3,1,3,1,1]:
    k.append(node(i))
    
    
root = k[0]
root.left = k[1]
root.left.left = k[3]
root.right = k[2]
root.right.right =k[-1]
root.left.right = k[-2]
    
    
a= Solution()
a.pseudoPalindromicPaths(root)

    
 
    

